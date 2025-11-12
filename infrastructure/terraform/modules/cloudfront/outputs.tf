output "distribution_id" {
  description = "CloudFront distribution ID"
  value       = aws_cloudfront_distribution.exam_distribution.id
}

output "distribution_arn" {
  description = "CloudFront distribution ARN"
  value       = aws_cloudfront_distribution.exam_distribution.arn
}

output "distribution_domain_name" {
  description = "CloudFront distribution domain name"
  value       = aws_cloudfront_distribution.exam_distribution.domain_name
}

output "distribution_hosted_zone_id" {
  description = "CloudFront distribution hosted zone ID"
  value       = aws_cloudfront_distribution.exam_distribution.hosted_zone_id
}