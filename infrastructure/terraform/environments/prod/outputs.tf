output "github_actions_role_arn" {
  description = "ARN of the GitHub Actions IAM role"
  value       = module.github_oidc.role_arn
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = module.s3.bucket_name
}

output "cloudfront_distribution_id" {
  description = "CloudFront distribution ID"
  value       = module.cloudfront.distribution_id
}

output "website_url" {
  description = "Website URL"
  value       = "https://${local.subdomain}"
}