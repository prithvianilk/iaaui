terraform{
    backend "s3"{
        region="ap-south-1"
        bucket="yg-hack-s3"
        key="yg-terraformstate/terraform.tfstate"
        access_key = "AKIA3EZCPWK3H2I2TYWH"
        secret_key = "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"
    }
}