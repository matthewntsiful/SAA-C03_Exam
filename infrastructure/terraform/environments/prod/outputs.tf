output "website_url" {
  description = "Website URL"
  value       = "https://${local.subdomain}"
}

output "s3_bucket_name" {
  description = "S3 bucket name"
  value       = module.s3.bucket_name
}

output "cloudfront_distribution_id" {
  description = "CloudFront distribution ID"
  value       = module.cloudfront.distribution_id
}

output "cloudfront_domain_name" {
  description = "CloudFront distribution domain name"
  value       = module.cloudfront.distribution_domain_name
}

output "github_actions_role_arn" {
  description = "GitHub Actions OIDC role ARN"
  value       = module.github_oidc.role_arn
}
