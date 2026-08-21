#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

echo "🚀 Initializing 're-engineering-the-software-engineering' repository structure..."

# 1. Define required directory structure
DIRS=(
  "chapters"
  "labs/lab-ci-cd-playground"
  "labs/lab-observability"
  "labs/lab-platform-quickstart"
  "templates"
  "assets"
  ".github/ISSUE_TEMPLATE"
  ".github/workflows"
)

for dir in "${DIRS[@]}"; do
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
    echo "  [+] Created directory: $dir"
  fi
done

# 2. Define Chapters
CHAPTERS=(
  "01-introduction.md"
  "02-diagnostics-and-metrics.md"
  "03-automation-first-ci-cd.md"
  "04-infra-as-code.md"
  "05-observability-and-verification.md"
  "06-platform-engineering.md"
  "07-quality-and-testing.md"
  "08-security-in-the-pipeline.md"
  "09-resilience-and-chaos.md"
  "10-operations-and-oncall.md"
  "11-developer-experience.md"
  "12-migration-and-adoption-guides.md"
  "13-measurement-and-feedback.md"
  "14-governance-and-policy.md"
  "15-case-studies-and-experiments.md"
)

# 3. Scaffold Chapter Files (if they don't exist yet)
for chapter in "${CHAPTERS[@]}"; do
  filepath="chapters/$chapter"
  if [ ! -f "$filepath" ]; then
    title=$(echo "$chapter" | sed -E 's/^[0-9]+-(.*)\.md$/\1/' | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)}1')
    cat <<EOF > "$filepath"
# Chapter: $title

## Problem Statement

## Principles & Decision Criteria

## Patterns & Anti-Patterns

## Implementation Recipes
### Minimal
### Recommended
### Advanced

## Playbook Checklists & Migration Steps

## Reproducible Examples & Labs

## Measurement & Success Criteria

## Further Reading & References
EOF
    echo "  [+] Scaffolding chapter: $filepath"
  fi
done

# 4. Create Baseline Template Files
touch templates/SLO-template.yaml
touch templates/Incident-playbook-template.md
touch templates/Migration-plan-template.md

# 5. Create Root Repository Files
touch CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE ROADMAP.md
touch labs/lab-ci-cd-playground/README.md
touch labs/lab-observability/README.md
touch labs/lab-platform-quickstart/README.md

echo "✅ Initialization complete!"