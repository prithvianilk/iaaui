image_name=$1

docker build -t $image_name ./temp/$image_name

aws configure --profile yg set aws_access_key_id $aws_access_key_id 
aws configure --profile yg set aws_secret_access_key $aws_secret_access_key 

aws ecr-public --profile yg get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/z2h9g2z1
docker tag $image_name:latest public.ecr.aws/z2h9g2z1/hack:$image_name
docker push public.ecr.aws/z2h9g2z1/hack:$image_name