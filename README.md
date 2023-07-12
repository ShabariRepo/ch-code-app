<Docker>

Docker tagging and run
- build the docker image
`docker build -t ch-code-app .`

Run the docker container
`docker run -d -p 8080:8080 ch-code-app`

<Helm/K8s>

- apply the deployment
`kubectl apply -f ./deployment.yml`

- apply the service
`kubectl apply -f service-lb.yml`

- if any changes are done to the python file or config map then will have to be applied again
- changes to python will warrant a image rebuild
- change to config will warrant a aplpy of config below
`kubectl apply -f configmap.yml`