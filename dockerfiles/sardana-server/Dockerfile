#FROM ubuntu:resolute-20260108
FROM mambaorg/micromamba:git-5f62561-cuda11.8.0-ubuntu22.04
USER root

RUN <<EOF
apt-get clean 
apt-get update 
apt-get upgrade -y
EOF

RUN <<EOF
apt-get install -y openjdk-8-jdk zlib1g-dev libomniorb4-dev libcos4-dev omniidl libzmq3-dev 
EOF

RUN useradd -ms /bin/bash tango 
USER tango
WORKDIR /home/tango

ARG PYTHON_VERSION=3.10
ARG PYTANGO_VERSION=9.3.6
#ARG SARDANA_VERSION=1.1.1

RUN <<EOF
micromamba install --yes \
python=$PYTHON_VERSION \
pytango=$PYTANGO_VERSION \
sardana \
h5py ipython itango
EOF

ENV PATH=/opt/conda/bin:$PATH

