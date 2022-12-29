terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.48.0"
    }
  }
}

provider "aws" {
  region = var.account_region
  access_key = var.user_access_key
  secret_key = var.user_secret_key
}
