#/bin/bash
sudo docker build -f ./docker/Dockerfile -t app:v2 ./app
sudo docker image tag app:v2 localhost:5000/app:v2
sudo docker push localhost:5000/app:v2