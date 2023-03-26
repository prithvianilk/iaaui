image_name=$1
base_folder=$2

# docker build -t $image_name -f ./dockerfiles/Dockerfile --platform linux/x86_64 $base_folder/$image_name

# aws ecr-public --profile yg get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/z2h9g2z1
# docker tag $image_name:latest public.ecr.aws/z2h9g2z1/hack:$image_name
# docker push public.ecr.aws/z2h9g2z1/hack:$image_name