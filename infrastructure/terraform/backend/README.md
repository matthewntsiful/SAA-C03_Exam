# Terraform Backend Infrastructure

This directory creates the S3 bucket and DynamoDB table needed for remote state management.

## Setup (One-time)

```bash
cd infrastructure/terraform/backend
terraform init
terraform apply
```

This creates:
- S3 bucket: `saa-exams-terraform-state` (versioned, encrypted)
- DynamoDB table: `terraform-state-locks` (for state locking)

## After Backend is Created

Update dev and prod environments to use remote backend.
