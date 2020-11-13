# Set the base image to jupyter
FROM tschm/jupyter:1.3.1 as jupyter

# copy the package over and install it
COPY --chown=jovyan:users ./requirements.txt /tmp/requirements.txt

USER root

RUN mkdir /var/lib/apt/lists/partial && \
    buildDeps='gcc' && \
    apt-get update && \
    apt-get install -y $buildDeps --no-install-recommends && \
    apt-get install -y libgmp3-dev --no-install-recommends && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt && \
    apt-get purge -y --auto-remove $buildDeps && \
    rm -rf /var/lib/apt/lists/partial

USER jovyan

COPY --chown=jovyan:100 ./work $WORK

WORKDIR /home/$NB_USER
