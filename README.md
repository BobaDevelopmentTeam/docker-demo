# docker-demo

This is the repository to complement the Pinned Workshop: Introduction to Docker.

It consists of two directories, src and docker.

`src` contains the src code necessary to run the Docker container. Essentially, any business logic goes here.

`docker` contains the code necessary to build, run, and deploy this either locally, on the cloud, or anywhere really.

## how to use


`cd docker`

`make build`
This will build the Dockerfile locally.

`make sandbox`
This will allow you to run the docker image and enter it, allowing you to perform commands inside of the docker image.

`make run` 
This runs the docker container locally with its default entrypoint. In our example, we use Flask and use port forwarding to port its port 5000 to our port 5000 to render the HTML.
