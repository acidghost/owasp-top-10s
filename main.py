import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import cast
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ORG_NAME = "OWASP"
SEARCH_API_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN_ENV_VAR = "GITHUB_TOKEN"
README_PATH = Path(__file__).resolve().with_name("README.md")
ARCHIVED_PATH = Path(__file__).resolve().with_name("archived.txt")
README_SECTION_START = "<!-- owasp-top-repos:start -->"
README_SECTION_END = "<!-- owasp-top-repos:end -->"
USER_AGENT = "owasp-top-10s"
TOP_NAME_PATTERN = re.compile(
    r"(^|[^A-Za-z0-9])top[A-Za-z0-9]*($|[^A-Za-z0-9])",
    re.IGNORECASE,
)
SEARCH_QUERY = f"org:{ORG_NAME} top in:name"
# Static display names for the repositories currently surfaced by this script.
REPOSITORY_DISPLAY_NAMES: dict[str, str] = {
    "Top10": "Top 10",
    "www-project-top-ten": "Proj Top Ten",
    "www-project-top-10-for-large-language-model-applications": "Top 10 for LLM Apps",
    "www-project-kubernetes-top-ten": "Kubernetes Top 10",
    "Serverless-Top-10-Project": "Serverless Top 10",
    "www-project-mobile-top-10": "Mobile Top 10",
    "www-project-top-10-ci-cd-security-risks": "Top 10 CI/CD Security Risks",
    "www-project-machine-learning-security-top-10": "Machine Learning Security Top 10",
    "www-project-citizen-development-top10-security-risks": "Citizen Development Top 10 Security Risks",
    "www-project-top-10-infrastructure-security-risks": "Top 10 Infrastructure Security Risks",
    "www-project-smart-contract-top-10": "Smart Contract Top 10",
    "www-project-agentic-skills-top-10": "Agentic Skills Top 10",
    "www-project-mcp-top-10": "MCP Top 10",
    "www-project-non-human-identities-top-10": "Non-Human Identities Top 10",
    "www-project-cloud-native-application-security-top-10": "Cloud Native Application Security Top 10",
    "Top-5-Machine-Learning-Risks": "Top 5 Machine Learning Risks",
    "www-project-top-25-parameters": "Top 25 Parameters",
    "www-project-operational-technology-top-10": "Operational Technology Top 10",
    "Cloud-Native-Application-Security-Top-10": "Cloud Native Application Security Top 10",
    "www-project-top-10-privacy-risks": "Top 10 Privacy Risks",
    "www-project-open-source-software-top-10": "Open Source Software Top 10",
    "www-project-serverless-top-10": "Serverless Top 10",
    "www-project-docker-top-10": "Docker Top 10",
    "www-project-devsecops-top-10": "DevSecOps Top 10",
    "www-project-top-10-client-side-security-risks": "Top 10 Client-Side Security Risks",
    "www-project-desktop-app-security-top-10": "Desktop App Security Top 10",
    "www-project-data-security-top-10": "Data Security Top 10",
    "www-project-internet-of-things-top-10": "Internet of Things Top 10",
    "www-project-solana-programs-top-10": "Solana Programs Top 10",
    "www-project-top-10-for-business-logic-abuse": "Top 10 for Business Logic Abuse",
    "www-project-top-10-for-maritime-security": "Top 10 for Maritime Security",
    "www-project-ai-top-ten": "AI Top 10",
    "www-project-attack-surface-management-top-10": "Attack Surface Management Top 10",
    "www-project-thick-client-top-10": "Thick Client Top 10",
    "www-project-top-10-the-game": "Top 10: The Game",
    "www-project-ot-top-ten": "OT Top 10",
    "www-project-top-10-drone-security-risks": "Top 10 Drone Security Risks",
    "www-project-top-10-in-xr": "Top 10 in XR",
    "www-project-top-ten-card-game": "Top 10 Card Game",
    "www-project-audio-video-communications-top-10": "Audio/Video Communications Top 10",
    "www-project-ot-top10-vulnerabilities-demonstrator": "OT Top 10 Vulnerabilities Demonstrator",
}

DEFAULT_README = f"""# OWASP repositories with "top" in the name

This repository contains a small stdlib-only script that queries the GitHub API
for repositories in the `{ORG_NAME}` organization whose names contain a `top`
token, updates the generated section below, and writes archived matches to
`archived.txt`.

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
    archived: bool


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


def require_bool(value: object, field_name: str) -> bool:
    if not isinstance(value, bool):
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
        archived=require_bool(item.get("archived"), "archived"),
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


def split_archived_repositories(
    repositories: list[Repository],
) -> tuple[list[Repository], list[Repository]]:
    active_repositories: list[Repository] = []
    archived_repositories: list[Repository] = []

    for repository in repositories:
        if repository.archived:
            archived_repositories.append(repository)
        else:
            active_repositories.append(repository)

    return active_repositories, archived_repositories


def format_table_cell(value: str | None) -> str:
    if not value:
        return "—"
    return " ".join(value.split()).replace("|", r"\|")


def get_repository_display_name(repository: Repository) -> str:
    return REPOSITORY_DISPLAY_NAMES.get(repository.name, repository.name)


def render_repository_table(repositories: list[Repository]) -> str:
    lines = [
        f"Found {len(repositories)} matching repositories (excluding archived repos).",
        "",
        "| Repository | Stars | Description |",
        "| --- | ---: | --- |",
    ]

    for repository in repositories:
        lines.append(
            f"| [{get_repository_display_name(repository)}]({repository.html_url}) | "
            f"{repository.stargazers_count:,} | "
            f"{format_table_cell(repository.description)} |"
        )

    return "\n".join(lines)


def render_archived_repositories(repositories: list[Repository]) -> str:
    return "".join(
        f"{name}\n"
        for name in sorted(
            (repository.name for repository in repositories), key=str.lower
        )
    )


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


def update_archived_file(repositories: list[Repository]) -> None:
    ARCHIVED_PATH.write_text(
        render_archived_repositories(repositories),
        encoding="utf-8",
    )


def main() -> int:
    token = os.getenv(GITHUB_TOKEN_ENV_VAR)
    candidate_repositories = fetch_matching_repositories(token)
    matching_repositories = filter_top_repositories(candidate_repositories)
    active_repositories, archived_repositories = split_archived_repositories(
        matching_repositories
    )
    update_readme(active_repositories)
    update_archived_file(archived_repositories)
    print(
        f"Updated {README_PATH.name} with {len(active_repositories)} repositories "
        f"and {ARCHIVED_PATH.name} with {len(archived_repositories)} archived repositories "
        f"from the {ORG_NAME} organization."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc
