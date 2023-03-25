image_name=$1
base_folder=$2
aws_access_key_id=$3
aws_secret_access_key=$4

docker build -t $image_name -f ./dockerfiles/Dockerfile --platform linux/x86_64 $base_folder/$image_name

aws configure --profile yg set aws_access_key_id $aws_access_key_id 
aws configure --profile yg set aws_secret_access_key $aws_secret_access_key 

aws ecr-public --profile yg get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/z2h9g2z1
docker tag $image_name:latest public.ecr.aws/z2h9g2z1/hack:$image_name
docker push public.ecr.aws/z2h9g2z1/hack:$image_name