import os
import logging

c = get_config()

# Setting Logging level to DEBUG
c.JupyterHub.log_level = logging.DEBUG

# Listen on all NIC when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'

# Authentication configuration
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.server_address = os.environ['LDAP_SERVER_ADDRESS']
c.LDAPAuthenticator.lookup_dn = True
# Uncomment this if you want to use SSL
# c.LDAPAuthenticator.use_ssl = True

# Launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# OR
# from dockerspawner import DockerSpawner
# c.JupyterHub.spawner_class = DockerSpawner

c.DockerSpawner.image = os.environ['DOCKER_SPAWNER_IMAGE']

# Delete containers when the stop
c.DockerSpawner.remove = True

c.DockerSpawner.extra_host_config = {'network_mode': 'host'}
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = 'host'

# Hostname/ip that should be used to connect to the hub
# c.JupyterHub.hub_connect_ip = 'jupyterhub'

# Docker network to connect to
# c.DockerSpawner.network_name = 'jupyterhub'