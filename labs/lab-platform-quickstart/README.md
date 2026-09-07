# Lab: Platform-as-a-Product & Self-Service Quickstart

## Objective
Experience the fundamentals of Internal Developer Platforms (IDPs) by executing a self-service CLI scaffolder that provisions a standardized Golden Path service template with variable substitution.

## Workflow
1. **Template Definition**: Standardized application boilerplate residing in `templates/fastapi-service`.
2. **Self-Service Engine**: `scaffold.py` script substituting team metadata into fresh service instances.
3. **Generated Service Output**: Standardized project directory generated inside `generated-services/`.

## Instructions

### 1. Run Scaffolding Tool
Generate a new service locally:
```bash
python3 scaffold.py order-service backend-core
