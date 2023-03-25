terraform {
 required_providers {
  aws = {
   source = "hashicorp/aws"
  }
 }
}

# variable "region" {
#   description = "AWS region"
#   type        = string
#   default     = "ap-south-1"
# }