# jupyterhub-docker-ldap

Docker image for JupyterHub with DockerSpawner and LDAPAuthenticator Configuration

---

## Configuration

- Create a `.env` file from `.env.example`
- Fill the environment variables:
  - DOCKER_SPAWNER_IMAGE="<>"
  - LDAP_SERVER_ADDRESS="<LDAP Server Address>"

---

## Pre-requisites

- Docker 
  - On Mac: `brew install docker`
  - All: `curl -fsSL https://get.docker.com/ | sh`
- Docker Compose - `brew install docker-compose`

---

## Running

### With Docker

```
sudo docker run --restart=always --name=jupyterhub -p 8000:8000 --env-file .env vs4vijay/jupyterhub-docker-ldap
```

- Use `-d` option if you want to start in background daemon

### With Docker Compose