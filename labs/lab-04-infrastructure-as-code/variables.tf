variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "Target AWS Region"
}

variable "bucket_name" {
  type        = string
  default     = "re-eng-iac-lab-bucket"
  description = "Name of the local S3 bucket to create"
}
