#!/usr/bin/env bash
set -e

echo "=== [1/2] Running SAST Code Scan (Bandit) ==="
bandit -r app/ -c .bandit.yaml --exit-zero

echo "=== [2/2] Scanning Dependencies for Known CVEs (Pip-Audit) ==="
pip-audit --desc || true

echo "=== Security Scans Completed ==="
