import os
import logging

# Setting Logging level to DEBUG
c.JupyterHub.log_level = logging.DEBUG

# Listen on all NIC when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'

# Authentication configuration
# If no auth variable is defined, then use dummy
auth = os.environ.get('AUTH')
if auth == 'DUMMY':
  c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
elif auth == 'LDAP':
  c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
  c.LDAPAuthenticator.server_address = os.environ['LDAP_SERVER_ADDRESS']
  c.LDAPAuthenticator.lookup_dn = True
  # Uncomment this if you want to use SSL
  c.LDAPAuthenticator.use_ssl = True

# Launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# OR
# from dockerspawner import DockerSpawner
# c.JupyterHub.spawner_class = DockerSpawner

c.DockerSpawner.image = os.environ['DOCKER_SPAWNER_IMAGE']

# Delete containers when the stop
c.DockerSpawner.remove = True


network_name = os.environ.get('DOCKER_NETWORK_NAME') or 'jupyterhub_network'                                             
c.DockerSpawner.use_internal_ip = True                                          
c.DockerSpawner.network_name = network_name                                     
c.DockerSpawner.extra_host_config = { 'network_mode': network_name } 



# Hostname/ip that should be used to connect to the hub
# Typically container name
c.JupyterHub.hub_connect_ip = os.environ.get('HUB_CONNECT_IP') or 'jupyterhub'

# Docker network to connect to
# c.DockerSpawner.network_name = 'jupyterhub'