terraform{
    backend "s3"{
        region="ap-south-1"
        bucket="yg-hack-s3"
        key="yg-terraformstate/terraform.tfstate"
        access_key = "<YOUR_KEY>"
        secret_key = "<YOUR_SECRET_KEY>"
    }
}