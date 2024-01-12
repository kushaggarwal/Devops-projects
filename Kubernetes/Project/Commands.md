```
1. Build docker image for backend - docker build -t <your-docker-hub-repository-name> .
2. Build docker image for frontend - docker build -t <your-docker-hub-repository-name> .
3. Update the backend-deployment.yaml and frontend-deployment.yaml with the images on the docker hub repository
4. Apply the deployment files
- kubectl apply -f backend-deployment.yaml
- kubectl apply -f frontend-deployment.yaml
```
