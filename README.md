# Simple python app deployed on microk8s cluster
Very simple web app in python deployed on microk8s cluster

(!) TODO: nginx


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


```
sudo microk8s kubectl apply -f ./db/mysql-pv.yaml
sudo microk8s kubectl apply -f ./db/mysql-deployment.yaml
```

## debug
```
microk8s kubectl describe deployment mysql
```

## connect to db by creating a pod with running mysql client container
```
sudo microk8s kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql -ppassword
```

# Destroy
```
microk8s kubectl delete -n default deployment python-app-deployment
```

# Refresh certs
```
microk8s refresh-certs
```

# Recommended setup
```
sudo sh -c "echo -n '{\n    "insecure-registries" : ["localhost:32000"] \n}\n' > /etc/docker/daemon.json"
sudo systemctl restart docker
sudo iptables -P FORWARD ACCEPT 
sudo apt-get install iptables-persistent
```


# Initial setup
```
microk8s.enable dashboard
token=$(microk8s kubectl -n kube-system get secret | grep default-token | cut -d " " -f1)
microk8s kubectl -n kube-system describe secret $token
````

## how to get URL:
```
microk8s kubectl describe service/kubernetes-dashboard -n kube-system
```

or run proxy
```
microk8s dashboard-proxy
```
