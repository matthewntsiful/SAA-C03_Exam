variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "cloudfront_distribution_arn" {
  description = "CloudFront distribution ARN for OAC"
  type        = string
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}