# jupyterhub-docker-ldap

Docker Image for JupyterHub with DockerSpawner and LDAPAuthenticator configuration

---

## Configuration

- Create a `.env` file from `.env.example`, and fill the values appropriately
- Fill the environment variables:
  - `AUTH=LDAP` # Change to `DUMMY` if you want to use dummy authentication
  - `LDAP_SERVER_ADDRESS=<LDAP Server Address>`
  - `DOCKER_SPAWNER_IMAGE=jupyterhub/singleuser` # No Need to change this
  - `DOCKER_NETWORK_NAME=jupyterhub_network` # No Need to change this
  - `HUB_CONNECT_IP=jupyterhub` # No Need to change this

---

## Pre-requisites

- Docker 
  - On Mac: `brew install docker`
  - All: `curl -fsSL https://get.docker.com/ | sh`
- Docker Compose - `brew install docker-compose`
- Create Network with `jupyterhub_network` name
  - Command: `docker network create jupyterhub_network` 

---

## Running

### With Docker

```
sudo docker run --restart=always --name=jupyterhub --network=jupyterhub_network -p 8000:8000 --env-file .env vs4vijay/jupyterhub-docker-ldap
```

- Use `-d` option if you want to start in background daemon

### With Docker Compose

- To Start: `docker-compose up`
- To Build and Start: `docker-compose up --build`
- To Stop: `docker-compose down`

---

### Development Notes

```python3

from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner


python3 -m pip install --no-cache --user dockerspawner jupyterhub-ldapauthenticator


```