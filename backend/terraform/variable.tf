variable "cluster_name"{
    description = "Name of the cluster"
    type=string
}

variable "ami_type" {
    description = "The type of AMI"
    type=string
}

variable "min_size" {
    description = "Minimum number of node groups"
}

variable "max_size" {
    description = "Maximum number of node groups"
}

variable "desired_size" {
    description = "Desired number of node groups"
}

variable "aws_region" {
    description = "AWS Region"
    type=string
}

# variable "aws_profile" {
#     description = "AWS Profile"
# }

variable "access_key" {
    description = "AWS Access Key"
    type = string
}

variable "secret_key" {
    description = "AWS Secret Access Key"
    type = string
}

variable "node_group_name" {
    description = "Name of the node group"
    type=string
}

variable "instance_type" {
    description = "Type of EC2 Instance to use"
    type=string
}

variable "vpc_id" {
    description = "vpc id"
    type=string
}

variable "private_subnet_ids" {
    description = "private subnets"
    type=list(string)
}