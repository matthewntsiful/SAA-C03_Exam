variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "root_domain" {
  description = "Root domain name"
  type        = string
  default     = "blakkbrother.com"
}

variable "github_org" {
  description = "GitHub organization or username"
  type        = string
}

variable "github_repo" {
  description = "GitHub repository name"
  type        = string
}