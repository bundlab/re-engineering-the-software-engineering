output "s3_bucket_arn" {
  value       = aws_s3_bucket.app_storage.arn
  description = "ARN of the provisioned local S3 bucket"
}

output "iam_role_arn" {
  value       = aws_iam_role.app_exec_role.arn
  description = "ARN of the provisioned local IAM Role"
}
