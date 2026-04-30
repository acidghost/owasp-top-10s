# OWASP Top 10s

[![Update OWASP top repos](https://github.com/acidghost/owasp-top-10s/actions/workflows/update.yaml/badge.svg)](https://github.com/acidghost/owasp-top-10s/actions/workflows/update.yaml)

This repository contains a small stdlib-only script that queries the GitHub API
for repositories in the `OWASP` organization whose names contain a `top`
token, updates the generated section below, and writes archived matches to
`archived.txt`.

## Usage

```bash
python3 main.py
GITHUB_TOKEN=your_token_here python3 main.py
```

## Generated repository list

<!-- owasp-top-repos:start -->
Found 34 matching repositories (excluding archived repos).

| Repository | Stars | Description |
| --- | ---: | --- |
| [Top 10](https://github.com/OWASP/Top10) | 5,580 | Official OWASP Top 10 Document Repository |
| [Proj Top Ten](https://github.com/OWASP/www-project-top-ten) | 1,384 | OWASP Foundation Web Respository |
| [Top 10 for LLM Apps](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) | 1,221 | OWASP Top 10 for Large Language Model Apps (Part of the GenAI Security Project) |
| [Kubernetes Top 10](https://github.com/OWASP/www-project-kubernetes-top-ten) | 610 | OWASP Foundation Web Respository |
| [Serverless Top 10](https://github.com/OWASP/Serverless-Top-10-Project) | 217 | OWASP Serverless Top 10 |
| [Mobile Top 10](https://github.com/OWASP/www-project-mobile-top-10) | 114 | — |
| [Top 10 CI/CD Security Risks](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) | 104 | OWASP Foundation Web Respository |
| [Machine Learning Security Top 10](https://github.com/OWASP/www-project-machine-learning-security-top-10) | 101 | OWASP Machine Learning Security Top 10 Project |
| [Citizen Development Top 10 Security Risks](https://github.com/OWASP/www-project-citizen-development-top10-security-risks) | 76 | OWASP Citizen Development Top 10 |
| [Top 10 Infrastructure Security Risks](https://github.com/OWASP/www-project-top-10-infrastructure-security-risks) | 73 | OWASP Top 10 Infrastructure Security Risks |
| [Smart Contract Top 10](https://github.com/OWASP/www-project-smart-contract-top-10) | 71 | OWASP Smart Contract Top 10 |
| [Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10) | 70 | OWASP Foundation web repository |
| [MCP Top 10](https://github.com/OWASP/www-project-mcp-top-10) | 63 | OWASP Foundation web repository |
| [Non-Human Identities Top 10](https://github.com/OWASP/www-project-non-human-identities-top-10) | 43 | OWASP Non-Human Identities Top 10 |
| [Top 25 Parameters](https://github.com/OWASP/www-project-top-25-parameters) | 26 | OWASP Foundation Web Respository |
| [Operational Technology Top 10](https://github.com/OWASP/www-project-operational-technology-top-10) | 23 | OWASP Foundation web repository |
| [Open Source Software Top 10](https://github.com/OWASP/www-project-open-source-software-top-10) | 16 | OWASP Top 10 Open Source Software Risks |
| [Serverless Top 10](https://github.com/OWASP/www-project-serverless-top-10) | 11 | OWASP Foundation Web Respository |
| [Docker Top 10](https://github.com/OWASP/www-project-docker-top-10) | 10 | OWASP Foundation Web Respository |
| [DevSecOps Top 10](https://github.com/OWASP/www-project-devsecops-top-10) | 7 | OWASP Foundation Web Respository |
| [Top 10 Client-Side Security Risks](https://github.com/OWASP/www-project-top-10-client-side-security-risks) | 7 | OWASP Foundation Web Respository |
| [Desktop App Security Top 10](https://github.com/OWASP/www-project-desktop-app-security-top-10) | 6 | OWASP Foundation Repository |
| [Data Security Top 10](https://github.com/OWASP/www-project-data-security-top-10) | 5 | OWASP Foundation Web Respository |
| [Solana Programs Top 10](https://github.com/OWASP/www-project-solana-programs-top-10) | 4 | OWASP Foundation Web Respository |
| [Top 10 for Business Logic Abuse](https://github.com/OWASP/www-project-top-10-for-business-logic-abuse) | 4 | OWASP Foundation web repository |
| [Top 10 for Maritime Security](https://github.com/OWASP/www-project-top-10-for-maritime-security) | 3 | OWASP Foundation web repository |
| [Attack Surface Management Top 10](https://github.com/OWASP/www-project-attack-surface-management-top-10) | 2 | OWASP Foundation web repository |
| [Thick Client Top 10](https://github.com/OWASP/www-project-thick-client-top-10) | 2 | OWASP Foundation Web Respository |
| [Top 10: The Game](https://github.com/OWASP/www-project-top-10-the-game) | 2 | OWASP Foundation web repository |
| [Top 10 Drone Security Risks](https://github.com/OWASP/www-project-top-10-drone-security-risks) | 1 | OWASP Foundation web repository |
| [Top 10 in XR](https://github.com/OWASP/www-project-top-10-in-xr) | 1 | OWASP Foundation Web Respository |
| [Top 10 Card Game](https://github.com/OWASP/www-project-top-ten-card-game) | 1 | OWASP Foundation web repository |
| [Audio/Video Communications Top 10](https://github.com/OWASP/www-project-audio-video-communications-top-10) | 0 | OWASP Foundation web repository |
| [OT Top 10 Vulnerabilities Demonstrator](https://github.com/OWASP/www-project-ot-top10-vulnerabilities-demonstrator) | 0 | OWASP Foundation web repository |
<!-- owasp-top-repos:end -->
