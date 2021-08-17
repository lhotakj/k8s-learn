# Simple python app deployed on microk8s cluster
Very simple web app in python deployed on microk8s cluster
TODO: nginx


## Run local registry

```
sudo docker run -d -p 5000:5000 --name registry registry:2

```

## Build and push
```
sudo docker build -f ./docker/Dockerfile -t app:latest ./app
sudo docker image tag app:latest localhost:5000/app:latest
sudo docker push localhost:5000/app:latest

```

## DEBUG: List of images on local repo
```
curl http://localhost:5000/v2/_catalog
```

# Deploy

```
microk8s kubectl apply -f ./kubernetes/deployment.yaml
```

# Destroy
```
microk8s kubectl delete -n default deployment python-app-deployment
```