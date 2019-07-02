# Set the base image to Ubuntu
FROM jupyter/datascience-notebook:d4cbf2f80a2a

# install rise
RUN conda install -c damianavila82 rise

ENV WORK=/home/jovyan/work

# COPY --chown=$NB_UID:$NB_UID ./work ${WORK}
COPY ./work ${WORK}

# copy the config file
COPY ./binder/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py

WORKDIR ${WORK}
