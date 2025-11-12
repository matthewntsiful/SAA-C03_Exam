variable "environment" {
  description = "Environment name"
  type        = string
}

variable "cloudfront_distribution_id" {
  description = "CloudFront distribution ID"
  type        = string
}

variable "waf_web_acl_name" {
  description = "WAF Web ACL name"
  type        = string
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
