# Description
This repository contains the configuration and commands required to
monitor Kubernetes clusters with Bluemedora's products.

## Usage

The process below should work for most customers. 
1) Verify you are pointed to the correct cluster and your kubectl environment is setup properly
```sh
kubectl cluster-info
```
2) Setup the LPU service account and permissions:
```sh
kubectl apply -f https://raw.githubusercontent.com/BlueMedoraPublic/bm-kube-lpu/master/bluemedora-lpu/bm-clusterrole.yaml
kubectl apply -f https://raw.githubusercontent.com/BlueMedoraPublic/bm-kube-lpu/master/bluemedora-lpu/bm-clusterrolebinding.yaml
kubectl apply -f https://raw.githubusercontent.com/BlueMedoraPublic/bm-kube-lpu/master/bluemedora-lpu/bm-role.yaml
kubectl apply -f https://raw.githubusercontent.com/BlueMedoraPublic/bm-kube-lpu/master/bluemedora-lpu/bm-rolebinding.yaml
kubectl apply -f https://raw.githubusercontent.com/BlueMedoraPublic/bm-kube-lpu/master/bluemedora-lpu/bm-serviceaccount.yaml
```
3) Obtain the bearer token for the service account to use when setting up the source within Bindplane or vROps
```sh
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep bluemedora | awk '{print $1}')
```

## Advance Usage

#### Prepare Kubernetes
1) Make sure the apiserver has been started with `--authorization-mode=RBAC`

2) If you have to change your configuration in order to enable this you will also need to pass `--authorization-rbac-super-user=admin` replacing 'admin' with whatever your admin account is.

3) Most Kubernetes deploy tools have RBAC enabled by default. If yours was not, you will need to do some additional setup in order to get everything running smoothly. This blog post has a step by step walkthrough: http://blog.screwdriver.cd/post/150999692902/how-we-got-rbac-working-in-kubernetes

4) You will need to restart the apiserver if you had to update the configuration to enable this.

#### Deploy LPU
Deploy and retrieve the bearer token
```sh
kubectl create -f bluemedora-lpu/
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep bluemedora | awk '{print $1}')
```
