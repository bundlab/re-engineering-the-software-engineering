# Lab 04: Infrastructure as Code (IaC) & Local Cloud Emulation

## Objective
Learn declarative infrastructure management by provisioning an S3 bucket and IAM execution role using Terraform or OpenTofu against a local AWS emulator (LocalStack).

## Prerequisites
* Docker & Docker Compose
* OpenTofu or Terraform CLI installed (`tofu` or `terraform`)

## Instructions

### 1. Start Local Cloud Infrastructure
```bash
docker compose up -d