VERSION=1.0.0
PROJECT=flask-website

build:
	docker build -f Dockerfile -t $(USER)/$(PROJECT):$(VERSION)-dev ..

# interactive mode
sandbox: build
	docker run -it --entrypoint /bin/bash $(USER)/$(PROJECT):$(VERSION)-dev

# dev mode
run: build
	docker run -p 5000:5000 $(USER)/$(PROJECT):$(VERSION)-dev

# build to docker hub/ecr

# push to docker hub/ecr