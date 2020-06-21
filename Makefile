PROJECT := 'jupyterhub-docker-ldap'

.PHONY: build
build:
	docker build -t $(PROJECT) .

.PHONY: run
push:
	sudo docker run --restart=always --name=jupyterhub -p 8000:8000 --env-file .env $(PROJECT)

.PHONY: push
push:
	docker push $(PROJECT)