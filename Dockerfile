FROM jupyter/base-notebook:latest
MAINTAINER Vijay Soni <vs4vijay@gmail.com>


ADD install_dep.sh /etc/jupyterhub/install_dep.sh
ADD jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

RUN bash /etc/jupyterhub/install_dep.sh

EXPOSE 8000

ENTRYPOINT ["jupyterhub"]

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]