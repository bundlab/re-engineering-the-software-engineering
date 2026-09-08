# Lab 07: Quality Gates and Automated Testing

## Objective
Implement automated unit and integration tests using Pytest, enforce code coverage thresholds (>80%), and configure isolated test execution via Docker.

## Quickstart

### 1. Run Tests Locally
```bash
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing