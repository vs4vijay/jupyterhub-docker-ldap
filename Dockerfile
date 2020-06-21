FROM jupyter/jupyterhub:latest
MAINTAINER Vijay Soni <vs4vijay@gmail.com>


ADD install_dep.sh /srv/jupyterhub/install_dep.sh
ADD jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

RUN ["install_dep.sh"]

EXPOSE 8000

ENTRYPOINT ["jupyterhub"]

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]