# Infrastructure

Infrastructure as Code for SAA-C03 practice exams platform.

## 🏗️ Terraform

```bash
cd terraform/environments/dev
terraform init
terraform plan
terraform apply
```

## 📁 Structure

- `terraform/modules/` - Reusable Terraform modules
- `terraform/environments/` - Environment-specific configurations
- `cloudformation-template.yaml` - Alternative CloudFormation template
- `deploy-to-s3.sh` - Direct S3 deployment script

## 🔧 Modules

- **S3** - Static website hosting
- **CloudFront** - CDN distribution
- **Route53** - DNS management
- **WAF** - Web application firewall