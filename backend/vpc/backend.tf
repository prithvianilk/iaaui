
terraform{
    backend "s3"{
        region="ap-south-1"
        bucket="yg-hack-s3"
        key="yg-vpc-terraformstate/terraform.tfstate"
        profile = "yg"
    }
}