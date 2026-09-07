# Lab: CI/CD Automation & Quality Gates

## Objective
Build and validate an automated CI/CD pipeline featuring automated unit testing, code linting gates, and Docker artifact builds.

## Workflow Pipeline Stages
1. **Lint & Test Gate**: Installs dependencies and runs `pytest` suites.
2. **Container Build Gate**: Builds a production-ready Docker container image upon successful test pass.

## Instructions

### Option A: Local Container Test Run
To test the pipeline execution locally using Docker Compose:
```bash
docker compose run --rm test-runner