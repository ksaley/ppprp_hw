#!/bin/bash


docker build -t myapp:latest -f docker/Dockerfile.app .
docker build -t myscript:latest -f docker/Dockerfile.script .

kubectl apply -f k8s/app-deployment.yaml
kubectl apply -f k8s/app-service.yaml
kubectl apply -f k8s/cronjob.yaml