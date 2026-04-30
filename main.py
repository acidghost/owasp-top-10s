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


@dataclass(frozen=True, slots=True)
class RepositoryMeta:
    display_name: str
    tags: tuple[str, ...]


# Static repository metadata for the repositories currently surfaced by this script.
REPOSITORY_METADATA: dict[str, RepositoryMeta] = {
    "Top10": RepositoryMeta(
        display_name="Top 10",
        tags=("application-security", "web-security"),
    ),
    "www-project-top-ten": RepositoryMeta(
        display_name="Proj Top Ten",
        tags=("application-security", "web-security"),
    ),
    "www-project-top-10-for-large-language-model-applications": RepositoryMeta(
        display_name="Top 10 for LLM Apps",
        tags=("ai-security", "application-security"),
    ),
    "www-project-kubernetes-top-ten": RepositoryMeta(
        display_name="Kubernetes Top 10",
        tags=("cloud-native", "infrastructure-security"),
    ),
    "Serverless-Top-10-Project": RepositoryMeta(
        display_name="Serverless Top 10",
        tags=("cloud-native",),
    ),
    "www-project-mobile-top-10": RepositoryMeta(
        display_name="Mobile Top 10",
        tags=("client-security", "application-security"),
    ),
    "www-project-top-10-ci-cd-security-risks": RepositoryMeta(
        display_name="Top 10 CI/CD Security Risks",
        tags=("software-supply-chain", "devsecops", "infrastructure-security"),
    ),
    "www-project-machine-learning-security-top-10": RepositoryMeta(
        display_name="Machine Learning Security Top 10",
        tags=("ai-security",),
    ),
    "www-project-citizen-development-top10-security-risks": RepositoryMeta(
        display_name="Citizen Development Top 10 Security Risks",
        tags=("application-security", "risk-management"),
    ),
    "www-project-top-10-infrastructure-security-risks": RepositoryMeta(
        display_name="Top 10 Infrastructure Security Risks",
        tags=("infrastructure-security",),
    ),
    "www-project-smart-contract-top-10": RepositoryMeta(
        display_name="Smart Contract Top 10",
        tags=("blockchain",),
    ),
    "www-project-agentic-skills-top-10": RepositoryMeta(
        display_name="Agentic Skills Top 10",
        tags=("ai-security", "devsecops"),
    ),
    "www-project-mcp-top-10": RepositoryMeta(
        display_name="MCP Top 10",
        tags=("ai-security", "devsecops"),
    ),
    "www-project-non-human-identities-top-10": RepositoryMeta(
        display_name="Non-Human Identities Top 10",
        tags=("cloud-native", "infrastructure-security"),
    ),
    "www-project-cloud-native-application-security-top-10": RepositoryMeta(
        display_name="Cloud Native Application Security Top 10",
        tags=("cloud-native", "application-security"),
    ),
    "Top-5-Machine-Learning-Risks": RepositoryMeta(
        display_name="Top 5 Machine Learning Risks",
        tags=("ai-security",),
    ),
    "www-project-top-25-parameters": RepositoryMeta(
        display_name="Top 25 Parameters",
        tags=("application-security", "security-assessment"),
    ),
    "www-project-operational-technology-top-10": RepositoryMeta(
        display_name="Operational Technology Top 10",
        tags=("cyber-physical-security", "infrastructure-security"),
    ),
    "Cloud-Native-Application-Security-Top-10": RepositoryMeta(
        display_name="Cloud Native Application Security Top 10",
        tags=("cloud-native", "application-security"),
    ),
    "www-project-top-10-privacy-risks": RepositoryMeta(
        display_name="Top 10 Privacy Risks",
        tags=("risk-management",),
    ),
    "www-project-open-source-software-top-10": RepositoryMeta(
        display_name="Open Source Software Top 10",
        tags=("software-supply-chain",),
    ),
    "www-project-serverless-top-10": RepositoryMeta(
        display_name="Serverless Top 10",
        tags=("cloud-native", "application-security"),
    ),
    "www-project-docker-top-10": RepositoryMeta(
        display_name="Docker Top 10",
        tags=("cloud-native", "infrastructure-security"),
    ),
    "www-project-devsecops-top-10": RepositoryMeta(
        display_name="DevSecOps Top 10",
        tags=("software-supply-chain", "devsecops"),
    ),
    "www-project-top-10-client-side-security-risks": RepositoryMeta(
        display_name="Top 10 Client-Side Security Risks",
        tags=("client-security", "web-security"),
    ),
    "www-project-desktop-app-security-top-10": RepositoryMeta(
        display_name="Desktop App Security Top 10",
        tags=("client-security", "application-security"),
    ),
    "www-project-data-security-top-10": RepositoryMeta(
        display_name="Data Security Top 10",
        tags=("infrastructure-security", "risk-management"),
    ),
    "www-project-internet-of-things-top-10": RepositoryMeta(
        display_name="Internet of Things Top 10",
        tags=("cyber-physical-security", "infrastructure-security"),
    ),
    "www-project-solana-programs-top-10": RepositoryMeta(
        display_name="Solana Programs Top 10",
        tags=("blockchain",),
    ),
    "www-project-top-10-for-business-logic-abuse": RepositoryMeta(
        display_name="Top 10 for Business Logic Abuse",
        tags=("application-security",),
    ),
    "www-project-top-10-for-maritime-security": RepositoryMeta(
        display_name="Top 10 for Maritime Security",
        tags=("cyber-physical-security", "infrastructure-security"),
    ),
    "www-project-ai-top-ten": RepositoryMeta(
        display_name="AI Top 10",
        tags=("ai-security",),
    ),
    "www-project-attack-surface-management-top-10": RepositoryMeta(
        display_name="Attack Surface Management Top 10",
        tags=("infrastructure-security", "security-assessment"),
    ),
    "www-project-thick-client-top-10": RepositoryMeta(
        display_name="Thick Client Top 10",
        tags=("client-security", "security-assessment"),
    ),
    "www-project-top-10-the-game": RepositoryMeta(
        display_name="Top 10: The Game",
        tags=("training",),
    ),
    "www-project-ot-top-ten": RepositoryMeta(
        display_name="OT Top 10",
        tags=("cyber-physical-security", "infrastructure-security"),
    ),
    "www-project-top-10-drone-security-risks": RepositoryMeta(
        display_name="Top 10 Drone Security Risks",
        tags=("cyber-physical-security",),
    ),
    "www-project-top-10-in-xr": RepositoryMeta(
        display_name="Top 10 in XR",
        tags=("client-security", "application-security"),
    ),
    "www-project-top-ten-card-game": RepositoryMeta(
        display_name="Top 10 Card Game",
        tags=("training",),
    ),
    "www-project-audio-video-communications-top-10": RepositoryMeta(
        display_name="Audio/Video Communications Top 10",
        tags=("client-security",),
    ),
    "www-project-ot-top10-vulnerabilities-demonstrator": RepositoryMeta(
        display_name="OT Top 10 Vulnerabilities Demonstrator",
        tags=("cyber-physical-security", "security-assessment"),
    ),
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
    metadata = REPOSITORY_METADATA.get(repository.name)
    if metadata is None:
        return repository.name
    return metadata.display_name


def get_repository_tags(repository: Repository) -> tuple[str, ...]:
    metadata = REPOSITORY_METADATA.get(repository.name)
    if metadata is None:
        return ()
    return metadata.tags


def get_repository_website_url(repository: Repository) -> str | None:
    if not repository.name.startswith("www-project"):
        return None
    return f"https://owasp.org/{repository.name}"


def render_repository_reference(repository: Repository) -> str:
    reference = f"[{get_repository_display_name(repository)}]({repository.html_url})"
    website_url = get_repository_website_url(repository)
    if website_url is None:
        return reference
    return f"{reference} ([🌐]({website_url}))"


def render_tag_link(tag: str) -> str:
    return f"[{tag}](#{tag})"


def render_repository_tags(repository: Repository) -> str:
    tags = get_repository_tags(repository)
    if not tags:
        return format_table_cell(None)
    return format_table_cell(", ".join(render_tag_link(tag) for tag in tags))


def render_tag_sections(repositories: list[Repository]) -> str:
    repositories_by_tag: dict[str, list[Repository]] = {}

    for repository in repositories:
        for tag in get_repository_tags(repository):
            repositories_by_tag.setdefault(tag, []).append(repository)

    if not repositories_by_tag:
        return ""

    lines = ["## Repositories by tag", ""]

    for tag in sorted(repositories_by_tag):
        lines.append(f"### {tag}")
        lines.append("")
        for repository in repositories_by_tag[tag]:
            lines.append(f"- {render_repository_reference(repository)}")
        lines.append("")

    return "\n".join(lines).rstrip()


def render_repository_table(repositories: list[Repository]) -> str:
    lines = [
        f"Found {len(repositories)} matching repositories (excluding archived repos).",
        "",
        "| Repository | Stars | Tags |",
        "| --- | ---: | --- |",
    ]

    for repository in repositories:
        tags = render_repository_tags(repository)
        lines.append(
            f"| {render_repository_reference(repository)} | "
            f"{repository.stargazers_count:,} | {tags} |"
        )

    return "\n".join(lines)


def render_repository_section(repositories: list[Repository]) -> str:
    table = render_repository_table(repositories)
    tag_sections = render_tag_sections(repositories)
    if not tag_sections:
        return table
    return f"{table}\n\n{tag_sections}"


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
    section_body = render_repository_section(repositories)
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
