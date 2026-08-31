# Chapter 04: Infrastructure as Code (IaC)

## Problem Statement

Manual infrastructure provisioning through cloud consoles ("ClickOps") and ad-hoc configuration shell scripts create unversioned, unreproducible environments prone to configuration drift, security vulnerabilities, and prolonged outages.

Modern software engineering requires **Infrastructure as Code (IaC)** where all platform resources—compute, networking, security policies, and managed services—are declared declaratively in version-controlled repositories, validated via automated test suites, and deployed through immutable continuous delivery pipelines.

---

## Principles & Decision Criteria

* **Declarative over Imperative:** Define the desired end-state of infrastructure assets using configuration languages rather than writing step-by-step shell execution scripts.
* **Single Source of Truth:** Treat repository state as the ground truth. No manual modifications or out-of-band emergency tweaks to cloud environments.
* **Immutability & Stateless Execution:** Destroy and replace compromised or outdated infrastructure resources rather than mutating running instances in place.
* **Policy-as-Code Guardrails:** Enforce security standards, compliance benchmarks, and tagging conventions automatically during the pull request phase before plan execution.

---

## Patterns & Anti-Patterns

| Category | Recommended Pattern | Anti-Pattern to Avoid |
| --- | --- | --- |
| **State Management** | **Remote State Locking:** Store state files in encrypted remote buckets (S3, GCS) with atomic locking mechanisms (DynamoDB, cloud locks). | **Local State Files:** Keeping state files on developer workstations or committing unencrypted state files containing sensitive secrets to Git. |
| **Module Architecture** | **DRY Reusable Modules:** Standardize infrastructure components into versioned, modular blocks with well-defined inputs and outputs. | **Monolithic Stack:** Writing multi-thousand-line single-file manifests where any change requires running plans across the entire environment. |
| **Drift Detection** | **Automated Drift Reconcilers:** Continuously scan cloud resources against IaC definitions and auto-remediate unauthorized manual changes. | **Manual Console Fixes:** Applying quick hotfixes or emergency security group changes via cloud web consoles without updating IaC code. |
| **Secret Provisioning** | **Dynamic Secret Injection:** Retrieve short-lived credentials at runtime via dynamic secret managers (HashiCorp Vault, AWS Secrets Manager). | **Hardcoded Secrets:** Storing plaintext credentials, database passwords, or private API keys directly inside IaC variable files or state files. |

---

## Implementation Recipes

### Minimal

* Declare core infrastructure components using standard HCL (Terraform/OpenTofu) or Crossplane.
* Store state files in a secure remote backend using automated state locking.
* Execute `plan` on pull requests and `apply` automatically upon merge to `main`.

### Recommended

* Organize infrastructure into composable, version-controlled modules with strict semantic versioning.
* Integrate static security analysis tools (e.g., `tfsec`, `checkov`, `trivy`) into CI pipelines to catch misconfigurations before deployment.
* Implement strict environment isolation using separate accounts or subscriptions per stage (Dev, Staging, Prod).

### Advanced

* Enforce Policy-as-Code checks (Open Policy Agent / Rego or Sentinel) to validate compliance, cost estimates, and security rules prior to pipeline execution.
* Adopt GitOps controllers (e.g., Crossplane or AWS Controllers for Kubernetes) to manage cloud infrastructure directly from Kubernetes CRDs.
* Deploy automated drift detection workflows that run scheduled daily plans and notify engineering teams via Slack/PagerDuty upon state divergence.

---

## Playbook Checklists & Migration Steps

1. **Audit Existing Cloud Assets:** Inventory unmanaged resources and generate import blocks to bring legacy infrastructure under IaC control.
2. **Standardize Module Layout:** Structure repositories using clean separation: `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`.
3. **Establish CI/CD Execution:** Lock down direct developer permissions to cloud environments; route all plan and apply steps exclusively through automated pipelines.
4. **Enforce Static Verification:** Add automated formatting (`terraform fmt -check`), validation, and linting steps to standard pull request workflows.

---

## Reproducible Examples & Labs

* [`labs/lab-iac-terraform-k8s`](https://www.google.com/search?q=../labs/lab-iac-terraform-k8s/) — Complete declarative infrastructure lab featuring remote state locking, security linting, and automated plan/apply workflows.

---

## Measurement & Success Criteria

* **IaC Coverage:** > 95% of active production cloud resources managed via version-controlled IaC code.
* **Configuration Drift Rate:** 0 unapproved manual console changes detected during daily automated drift audits.
* **Provisioning Speed:** Average time to spin up a fully compliant, isolated staging environment under 15 minutes.

---

## Further Reading & References

* Morris, K. (2020). *Infrastructure as Code: Dynamic Systems Integration for Cloud Age*. O'Reilly Media.
* Brikman, Y. (2022). *Terraform: Up & Running: Writing Infrastructure as Code*. O'Reilly Media.

---