NS ?= samzillard
VERSION ?= latest

VOLUMES = -v /var/run/docker.sock=/var/run/docker.sock
PORTS = -p 5000:5000
ENV = -e USER= -e PASSWORD=
IMAGE_NAME ?= yeet
CONTAINER_NAME ?= yeet
CONTAINER_INSTANCE ?= default

.PHONY: install start stop prune

start: Dockerfile
	docker build -t $(NS)/$(IMAGE_NAME):$(VERSION) -f Dockerfile .
	docker run -d --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(IMAGE_NAME):$(VERSION)

stop:
	docker stop $(CONTAINER_NAME)-$(CONTAINER_INSTANCE)
	docker rm $(CONTAINER_NAME)-$(CONTAINER_INSTANCE)

prune:
	docker system prune -a

default: build
