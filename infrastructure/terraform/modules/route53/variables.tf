variable "root_domain" {
  description = "Root domain name"
  type        = string
}

variable "subdomain" {
  description = "Subdomain name"
  type        = string
}

variable "cloudfront_domain_name" {
  description = "CloudFront distribution domain name"
  type        = string
}

variable "cloudfront_hosted_zone_id" {
  description = "CloudFront distribution hosted zone ID"
  type        = string
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}