PROJECT := 'jupyterhub-docker-ldap'

.PHONY: build
build:
	docker build -t $(PROJECT) .

.PHONY: run
push:
	sudo docker run --name=jupyterhub --restart=always --network=jupyterhub_network -p 8000:8000 --env-file .env $(PROJECT)

.PHONY: push
push:
	docker push $(PROJECT)