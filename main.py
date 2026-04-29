from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import cast
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ORG_NAME = "OWASP"
SEARCH_API_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN_ENV_VAR = "GITHUB_TOKEN"
README_PATH = Path(__file__).resolve().with_name("README.md")
README_SECTION_START = "<!-- owasp-top-repos:start -->"
README_SECTION_END = "<!-- owasp-top-repos:end -->"
USER_AGENT = "owasp-top-10s"
TOP_NAME_PATTERN = re.compile(
    r"(^|[^A-Za-z0-9])top[A-Za-z0-9]*($|[^A-Za-z0-9])",
    re.IGNORECASE,
)
SEARCH_QUERY = f"org:{ORG_NAME} top in:name"

DEFAULT_README = f"""# OWASP repositories with "top" in the name

This repository contains a small stdlib-only script that queries the GitHub API
for repositories in the `{ORG_NAME}` organization whose names contain a `top`
token, and updates the generated section below.

## Usage

```bash
python3 main.py
GITHUB_TOKEN=your_token_here python3 main.py
```

## Generated repository list

{README_SECTION_START}
Generated content will be inserted here.
{README_SECTION_END}
"""


@dataclass(slots=True)
class Repository:
    name: str
    full_name: str
    html_url: str
    stargazers_count: int
    description: str | None


def build_headers(token: str | None) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token.strip()}"
    return headers


def request_json(url: str, token: str | None) -> object:
    request = Request(url, headers=build_headers(token))

    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace").strip()
        message = f"GitHub API request failed with {exc.code} {exc.reason}."
        if details:
            message = f"{message}\n{details}"
        raise RuntimeError(message) from exc
    except URLError as exc:
        raise RuntimeError(f"Unable to reach the GitHub API: {exc.reason}") from exc


def require_object(value: object, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise RuntimeError(f"Unexpected {context} payload from the GitHub API.")
    return cast(dict[str, object], value)


def require_str(value: object, field_name: str) -> str:
    if not isinstance(value, str):
        raise RuntimeError(
            f"Unexpected type for {field_name!r} in the GitHub API response."
        )
    return value


def require_int(value: object, field_name: str) -> int:
    if not isinstance(value, int):
        raise RuntimeError(
            f"Unexpected type for {field_name!r} in the GitHub API response."
        )
    return value


def require_optional_str(value: object, field_name: str) -> str | None:
    if value is None or isinstance(value, str):
        return value
    raise RuntimeError(
        f"Unexpected type for {field_name!r} in the GitHub API response."
    )


def parse_repository(value: object) -> Repository:
    item = require_object(value, "repository")
    return Repository(
        name=require_str(item.get("name"), "name"),
        full_name=require_str(item.get("full_name"), "full_name"),
        html_url=require_str(item.get("html_url"), "html_url"),
        stargazers_count=require_int(
            item.get("stargazers_count"),
            "stargazers_count",
        ),
        description=require_optional_str(item.get("description"), "description"),
    )


def fetch_search_page(page: int, token: str | None) -> tuple[int, list[Repository]]:
    query = urlencode({"q": SEARCH_QUERY, "per_page": 100, "page": page})
    payload = require_object(request_json(f"{SEARCH_API_URL}?{query}", token), "search")

    total_count = require_int(payload.get("total_count"), "total_count")
    items = payload.get("items")
    if not isinstance(items, list):
        raise RuntimeError("Unexpected type for 'items' in the GitHub API response.")

    return total_count, [parse_repository(item) for item in items]


def fetch_matching_repositories(token: str | None) -> list[Repository]:
    repositories: list[Repository] = []
    page = 1

    while True:
        total_count, page_items = fetch_search_page(page, token)
        if not page_items:
            break
        repositories.extend(page_items)
        if len(repositories) >= total_count:
            break
        page += 1

    return repositories


def name_contains_top(name: str) -> bool:
    return TOP_NAME_PATTERN.search(name) is not None


def filter_top_repositories(repositories: list[Repository]) -> list[Repository]:
    return sorted(
        (
            repository
            for repository in repositories
            if name_contains_top(repository.name)
        ),
        key=lambda repository: (-repository.stargazers_count, repository.name.lower()),
    )


def format_table_cell(value: str | None) -> str:
    if not value:
        return "—"
    return " ".join(value.split()).replace("|", r"\|")


def render_repository_table(repositories: list[Repository]) -> str:
    timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        f"Found {len(repositories)} matching repositories.",
        "",
        f"_Last updated: {timestamp}_",
        "",
        "| Repository | Stars | Description |",
        "| --- | ---: | --- |",
    ]

    for repository in repositories:
        lines.append(
            f"| [{repository.full_name}]({repository.html_url}) | "
            f"{repository.stargazers_count:,} | "
            f"{format_table_cell(repository.description)} |"
        )

    return "\n".join(lines)


def ensure_readme_exists() -> None:
    if not README_PATH.exists() or not README_PATH.read_text(encoding="utf-8").strip():
        README_PATH.write_text(DEFAULT_README, encoding="utf-8")


def replace_generated_section(readme_text: str, section_body: str) -> str:
    if README_SECTION_START not in readme_text or README_SECTION_END not in readme_text:
        trimmed = readme_text.rstrip()
        if trimmed:
            readme_text = (
                f"{trimmed}\n\n## Generated repository list\n\n"
                f"{README_SECTION_START}\nplaceholder\n{README_SECTION_END}\n"
            )
        else:
            readme_text = DEFAULT_README

    start_index = readme_text.index(README_SECTION_START)
    end_index = readme_text.index(README_SECTION_END) + len(README_SECTION_END)
    replacement = f"{README_SECTION_START}\n{section_body}\n{README_SECTION_END}"
    return f"{readme_text[:start_index]}{replacement}{readme_text[end_index:]}"


def update_readme(repositories: list[Repository]) -> None:
    ensure_readme_exists()
    current_readme = README_PATH.read_text(encoding="utf-8")
    section_body = render_repository_table(repositories)
    updated_readme = replace_generated_section(current_readme, section_body)
    README_PATH.write_text(updated_readme, encoding="utf-8")


def main() -> int:
    token = os.getenv(GITHUB_TOKEN_ENV_VAR)
    candidate_repositories = fetch_matching_repositories(token)
    matching_repositories = filter_top_repositories(candidate_repositories)
    update_readme(matching_repositories)
    print(
        f"Updated {README_PATH.name} with {len(matching_repositories)} repositories "
        f"from the {ORG_NAME} organization."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc
