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

| Repository | Stars | Tags |
| --- | ---: | --- |
| [Top 10](https://github.com/OWASP/Top10) | 5,590 | [application-security](#application-security), [web-security](#web-security) |
| [Proj Top Ten](https://github.com/OWASP/www-project-top-ten) ([🌐](https://owasp.org/www-project-top-ten)) | 1,386 | [application-security](#application-security), [web-security](#web-security) |
| [Top 10 for LLM Apps](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) ([🌐](https://owasp.org/www-project-top-10-for-large-language-model-applications)) | 1,228 | [ai-security](#ai-security), [application-security](#application-security) |
| [Kubernetes Top 10](https://github.com/OWASP/www-project-kubernetes-top-ten) ([🌐](https://owasp.org/www-project-kubernetes-top-ten)) | 610 | [cloud-native](#cloud-native), [infrastructure-security](#infrastructure-security) |
| [Serverless Top 10](https://github.com/OWASP/Serverless-Top-10-Project) | 217 | [cloud-native](#cloud-native) |
| [Mobile Top 10](https://github.com/OWASP/www-project-mobile-top-10) ([🌐](https://owasp.org/www-project-mobile-top-10)) | 114 | [client-security](#client-security), [application-security](#application-security) |
| [Top 10 CI/CD Security Risks](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) ([🌐](https://owasp.org/www-project-top-10-ci-cd-security-risks)) | 104 | [software-supply-chain](#software-supply-chain), [devsecops](#devsecops), [infrastructure-security](#infrastructure-security) |
| [Machine Learning Security Top 10](https://github.com/OWASP/www-project-machine-learning-security-top-10) ([🌐](https://owasp.org/www-project-machine-learning-security-top-10)) | 101 | [ai-security](#ai-security) |
| [Citizen Development Top 10 Security Risks](https://github.com/OWASP/www-project-citizen-development-top10-security-risks) ([🌐](https://owasp.org/www-project-citizen-development-top10-security-risks)) | 76 | [application-security](#application-security), [risk-management](#risk-management) |
| [Top 10 Infrastructure Security Risks](https://github.com/OWASP/www-project-top-10-infrastructure-security-risks) ([🌐](https://owasp.org/www-project-top-10-infrastructure-security-risks)) | 73 | [infrastructure-security](#infrastructure-security) |
| [Smart Contract Top 10](https://github.com/OWASP/www-project-smart-contract-top-10) ([🌐](https://owasp.org/www-project-smart-contract-top-10)) | 72 | [blockchain](#blockchain) |
| [Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10) ([🌐](https://owasp.org/www-project-agentic-skills-top-10)) | 70 | [ai-security](#ai-security), [devsecops](#devsecops) |
| [MCP Top 10](https://github.com/OWASP/www-project-mcp-top-10) ([🌐](https://owasp.org/www-project-mcp-top-10)) | 64 | [ai-security](#ai-security), [devsecops](#devsecops) |
| [Non-Human Identities Top 10](https://github.com/OWASP/www-project-non-human-identities-top-10) ([🌐](https://owasp.org/www-project-non-human-identities-top-10)) | 43 | [cloud-native](#cloud-native), [infrastructure-security](#infrastructure-security) |
| [Top 25 Parameters](https://github.com/OWASP/www-project-top-25-parameters) ([🌐](https://owasp.org/www-project-top-25-parameters)) | 26 | [application-security](#application-security), [security-assessment](#security-assessment) |
| [Operational Technology Top 10](https://github.com/OWASP/www-project-operational-technology-top-10) ([🌐](https://owasp.org/www-project-operational-technology-top-10)) | 23 | [cyber-physical-security](#cyber-physical-security), [infrastructure-security](#infrastructure-security) |
| [Open Source Software Top 10](https://github.com/OWASP/www-project-open-source-software-top-10) ([🌐](https://owasp.org/www-project-open-source-software-top-10)) | 16 | [software-supply-chain](#software-supply-chain) |
| [Serverless Top 10](https://github.com/OWASP/www-project-serverless-top-10) ([🌐](https://owasp.org/www-project-serverless-top-10)) | 11 | [cloud-native](#cloud-native), [application-security](#application-security) |
| [Docker Top 10](https://github.com/OWASP/www-project-docker-top-10) ([🌐](https://owasp.org/www-project-docker-top-10)) | 10 | [cloud-native](#cloud-native), [infrastructure-security](#infrastructure-security) |
| [DevSecOps Top 10](https://github.com/OWASP/www-project-devsecops-top-10) ([🌐](https://owasp.org/www-project-devsecops-top-10)) | 7 | [software-supply-chain](#software-supply-chain), [devsecops](#devsecops) |
| [Top 10 Client-Side Security Risks](https://github.com/OWASP/www-project-top-10-client-side-security-risks) ([🌐](https://owasp.org/www-project-top-10-client-side-security-risks)) | 7 | [client-security](#client-security), [web-security](#web-security) |
| [Desktop App Security Top 10](https://github.com/OWASP/www-project-desktop-app-security-top-10) ([🌐](https://owasp.org/www-project-desktop-app-security-top-10)) | 6 | [client-security](#client-security), [application-security](#application-security) |
| [Data Security Top 10](https://github.com/OWASP/www-project-data-security-top-10) ([🌐](https://owasp.org/www-project-data-security-top-10)) | 5 | [infrastructure-security](#infrastructure-security), [risk-management](#risk-management) |
| [Solana Programs Top 10](https://github.com/OWASP/www-project-solana-programs-top-10) ([🌐](https://owasp.org/www-project-solana-programs-top-10)) | 4 | [blockchain](#blockchain) |
| [Top 10 for Business Logic Abuse](https://github.com/OWASP/www-project-top-10-for-business-logic-abuse) ([🌐](https://owasp.org/www-project-top-10-for-business-logic-abuse)) | 4 | [application-security](#application-security) |
| [Top 10 for Maritime Security](https://github.com/OWASP/www-project-top-10-for-maritime-security) ([🌐](https://owasp.org/www-project-top-10-for-maritime-security)) | 3 | [cyber-physical-security](#cyber-physical-security), [infrastructure-security](#infrastructure-security) |
| [Attack Surface Management Top 10](https://github.com/OWASP/www-project-attack-surface-management-top-10) ([🌐](https://owasp.org/www-project-attack-surface-management-top-10)) | 2 | [infrastructure-security](#infrastructure-security), [security-assessment](#security-assessment) |
| [Thick Client Top 10](https://github.com/OWASP/www-project-thick-client-top-10) ([🌐](https://owasp.org/www-project-thick-client-top-10)) | 2 | [client-security](#client-security), [security-assessment](#security-assessment) |
| [Top 10: The Game](https://github.com/OWASP/www-project-top-10-the-game) ([🌐](https://owasp.org/www-project-top-10-the-game)) | 2 | [training](#training) |
| [Top 10 Drone Security Risks](https://github.com/OWASP/www-project-top-10-drone-security-risks) ([🌐](https://owasp.org/www-project-top-10-drone-security-risks)) | 1 | [cyber-physical-security](#cyber-physical-security) |
| [Top 10 in XR](https://github.com/OWASP/www-project-top-10-in-xr) ([🌐](https://owasp.org/www-project-top-10-in-xr)) | 1 | [client-security](#client-security), [application-security](#application-security) |
| [Top 10 Card Game](https://github.com/OWASP/www-project-top-ten-card-game) ([🌐](https://owasp.org/www-project-top-ten-card-game)) | 1 | [training](#training) |
| [Audio/Video Communications Top 10](https://github.com/OWASP/www-project-audio-video-communications-top-10) ([🌐](https://owasp.org/www-project-audio-video-communications-top-10)) | 0 | [client-security](#client-security) |
| [OT Top 10 Vulnerabilities Demonstrator](https://github.com/OWASP/www-project-ot-top10-vulnerabilities-demonstrator) ([🌐](https://owasp.org/www-project-ot-top10-vulnerabilities-demonstrator)) | 0 | [cyber-physical-security](#cyber-physical-security), [security-assessment](#security-assessment) |

## Repositories by tag

### ai-security

- [Top 10 for LLM Apps](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) ([🌐](https://owasp.org/www-project-top-10-for-large-language-model-applications))
- [Machine Learning Security Top 10](https://github.com/OWASP/www-project-machine-learning-security-top-10) ([🌐](https://owasp.org/www-project-machine-learning-security-top-10))
- [Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10) ([🌐](https://owasp.org/www-project-agentic-skills-top-10))
- [MCP Top 10](https://github.com/OWASP/www-project-mcp-top-10) ([🌐](https://owasp.org/www-project-mcp-top-10))

### application-security

- [Top 10](https://github.com/OWASP/Top10)
- [Proj Top Ten](https://github.com/OWASP/www-project-top-ten) ([🌐](https://owasp.org/www-project-top-ten))
- [Top 10 for LLM Apps](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) ([🌐](https://owasp.org/www-project-top-10-for-large-language-model-applications))
- [Mobile Top 10](https://github.com/OWASP/www-project-mobile-top-10) ([🌐](https://owasp.org/www-project-mobile-top-10))
- [Citizen Development Top 10 Security Risks](https://github.com/OWASP/www-project-citizen-development-top10-security-risks) ([🌐](https://owasp.org/www-project-citizen-development-top10-security-risks))
- [Top 25 Parameters](https://github.com/OWASP/www-project-top-25-parameters) ([🌐](https://owasp.org/www-project-top-25-parameters))
- [Serverless Top 10](https://github.com/OWASP/www-project-serverless-top-10) ([🌐](https://owasp.org/www-project-serverless-top-10))
- [Desktop App Security Top 10](https://github.com/OWASP/www-project-desktop-app-security-top-10) ([🌐](https://owasp.org/www-project-desktop-app-security-top-10))
- [Top 10 for Business Logic Abuse](https://github.com/OWASP/www-project-top-10-for-business-logic-abuse) ([🌐](https://owasp.org/www-project-top-10-for-business-logic-abuse))
- [Top 10 in XR](https://github.com/OWASP/www-project-top-10-in-xr) ([🌐](https://owasp.org/www-project-top-10-in-xr))

### blockchain

- [Smart Contract Top 10](https://github.com/OWASP/www-project-smart-contract-top-10) ([🌐](https://owasp.org/www-project-smart-contract-top-10))
- [Solana Programs Top 10](https://github.com/OWASP/www-project-solana-programs-top-10) ([🌐](https://owasp.org/www-project-solana-programs-top-10))

### client-security

- [Mobile Top 10](https://github.com/OWASP/www-project-mobile-top-10) ([🌐](https://owasp.org/www-project-mobile-top-10))
- [Top 10 Client-Side Security Risks](https://github.com/OWASP/www-project-top-10-client-side-security-risks) ([🌐](https://owasp.org/www-project-top-10-client-side-security-risks))
- [Desktop App Security Top 10](https://github.com/OWASP/www-project-desktop-app-security-top-10) ([🌐](https://owasp.org/www-project-desktop-app-security-top-10))
- [Thick Client Top 10](https://github.com/OWASP/www-project-thick-client-top-10) ([🌐](https://owasp.org/www-project-thick-client-top-10))
- [Top 10 in XR](https://github.com/OWASP/www-project-top-10-in-xr) ([🌐](https://owasp.org/www-project-top-10-in-xr))
- [Audio/Video Communications Top 10](https://github.com/OWASP/www-project-audio-video-communications-top-10) ([🌐](https://owasp.org/www-project-audio-video-communications-top-10))

### cloud-native

- [Kubernetes Top 10](https://github.com/OWASP/www-project-kubernetes-top-ten) ([🌐](https://owasp.org/www-project-kubernetes-top-ten))
- [Serverless Top 10](https://github.com/OWASP/Serverless-Top-10-Project)
- [Non-Human Identities Top 10](https://github.com/OWASP/www-project-non-human-identities-top-10) ([🌐](https://owasp.org/www-project-non-human-identities-top-10))
- [Serverless Top 10](https://github.com/OWASP/www-project-serverless-top-10) ([🌐](https://owasp.org/www-project-serverless-top-10))
- [Docker Top 10](https://github.com/OWASP/www-project-docker-top-10) ([🌐](https://owasp.org/www-project-docker-top-10))

### cyber-physical-security

- [Operational Technology Top 10](https://github.com/OWASP/www-project-operational-technology-top-10) ([🌐](https://owasp.org/www-project-operational-technology-top-10))
- [Top 10 for Maritime Security](https://github.com/OWASP/www-project-top-10-for-maritime-security) ([🌐](https://owasp.org/www-project-top-10-for-maritime-security))
- [Top 10 Drone Security Risks](https://github.com/OWASP/www-project-top-10-drone-security-risks) ([🌐](https://owasp.org/www-project-top-10-drone-security-risks))
- [OT Top 10 Vulnerabilities Demonstrator](https://github.com/OWASP/www-project-ot-top10-vulnerabilities-demonstrator) ([🌐](https://owasp.org/www-project-ot-top10-vulnerabilities-demonstrator))

### devsecops

- [Top 10 CI/CD Security Risks](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) ([🌐](https://owasp.org/www-project-top-10-ci-cd-security-risks))
- [Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10) ([🌐](https://owasp.org/www-project-agentic-skills-top-10))
- [MCP Top 10](https://github.com/OWASP/www-project-mcp-top-10) ([🌐](https://owasp.org/www-project-mcp-top-10))
- [DevSecOps Top 10](https://github.com/OWASP/www-project-devsecops-top-10) ([🌐](https://owasp.org/www-project-devsecops-top-10))

### infrastructure-security

- [Kubernetes Top 10](https://github.com/OWASP/www-project-kubernetes-top-ten) ([🌐](https://owasp.org/www-project-kubernetes-top-ten))
- [Top 10 CI/CD Security Risks](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) ([🌐](https://owasp.org/www-project-top-10-ci-cd-security-risks))
- [Top 10 Infrastructure Security Risks](https://github.com/OWASP/www-project-top-10-infrastructure-security-risks) ([🌐](https://owasp.org/www-project-top-10-infrastructure-security-risks))
- [Non-Human Identities Top 10](https://github.com/OWASP/www-project-non-human-identities-top-10) ([🌐](https://owasp.org/www-project-non-human-identities-top-10))
- [Operational Technology Top 10](https://github.com/OWASP/www-project-operational-technology-top-10) ([🌐](https://owasp.org/www-project-operational-technology-top-10))
- [Docker Top 10](https://github.com/OWASP/www-project-docker-top-10) ([🌐](https://owasp.org/www-project-docker-top-10))
- [Data Security Top 10](https://github.com/OWASP/www-project-data-security-top-10) ([🌐](https://owasp.org/www-project-data-security-top-10))
- [Top 10 for Maritime Security](https://github.com/OWASP/www-project-top-10-for-maritime-security) ([🌐](https://owasp.org/www-project-top-10-for-maritime-security))
- [Attack Surface Management Top 10](https://github.com/OWASP/www-project-attack-surface-management-top-10) ([🌐](https://owasp.org/www-project-attack-surface-management-top-10))

### risk-management

- [Citizen Development Top 10 Security Risks](https://github.com/OWASP/www-project-citizen-development-top10-security-risks) ([🌐](https://owasp.org/www-project-citizen-development-top10-security-risks))
- [Data Security Top 10](https://github.com/OWASP/www-project-data-security-top-10) ([🌐](https://owasp.org/www-project-data-security-top-10))

### security-assessment

- [Top 25 Parameters](https://github.com/OWASP/www-project-top-25-parameters) ([🌐](https://owasp.org/www-project-top-25-parameters))
- [Attack Surface Management Top 10](https://github.com/OWASP/www-project-attack-surface-management-top-10) ([🌐](https://owasp.org/www-project-attack-surface-management-top-10))
- [Thick Client Top 10](https://github.com/OWASP/www-project-thick-client-top-10) ([🌐](https://owasp.org/www-project-thick-client-top-10))
- [OT Top 10 Vulnerabilities Demonstrator](https://github.com/OWASP/www-project-ot-top10-vulnerabilities-demonstrator) ([🌐](https://owasp.org/www-project-ot-top10-vulnerabilities-demonstrator))

### software-supply-chain

- [Top 10 CI/CD Security Risks](https://github.com/OWASP/www-project-top-10-ci-cd-security-risks) ([🌐](https://owasp.org/www-project-top-10-ci-cd-security-risks))
- [Open Source Software Top 10](https://github.com/OWASP/www-project-open-source-software-top-10) ([🌐](https://owasp.org/www-project-open-source-software-top-10))
- [DevSecOps Top 10](https://github.com/OWASP/www-project-devsecops-top-10) ([🌐](https://owasp.org/www-project-devsecops-top-10))

### training

- [Top 10: The Game](https://github.com/OWASP/www-project-top-10-the-game) ([🌐](https://owasp.org/www-project-top-10-the-game))
- [Top 10 Card Game](https://github.com/OWASP/www-project-top-ten-card-game) ([🌐](https://owasp.org/www-project-top-ten-card-game))

### web-security

- [Top 10](https://github.com/OWASP/Top10)
- [Proj Top Ten](https://github.com/OWASP/www-project-top-ten) ([🌐](https://owasp.org/www-project-top-ten))
- [Top 10 Client-Side Security Risks](https://github.com/OWASP/www-project-top-10-client-side-security-risks) ([🌐](https://owasp.org/www-project-top-10-client-side-security-risks))
<!-- owasp-top-repos:end -->
