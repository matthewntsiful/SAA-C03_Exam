output "bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.exam_bucket.id
}

output "bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.exam_bucket.arn
}

output "website_endpoint" {
  description = "Website endpoint for the S3 bucket"
  value       = aws_s3_bucket_website_configuration.exam_website.website_endpoint
}

output "bucket_domain_name" {
  description = "Domain name of the S3 bucket"
  value       = aws_s3_bucket.exam_bucket.bucket_domain_name
}

output "oac_id" {
  description = "Origin Access Control ID"
  value       = aws_cloudfront_origin_access_control.exam_oac.id
}

output "logs_bucket_domain_name" {
  description = "Domain name of the logs bucket"
  value       = aws_s3_bucket.logs.bucket_domain_name
}