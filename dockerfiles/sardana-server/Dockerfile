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

ARG PYTHON_VERSION=3.12
ARG NUMPY_VERSION=1.26.4
ARG PYTANGO_VERSION=10.1.4
ARG SARDANA_VERSION=3.6.0

RUN micromamba install --yes \
python=$PYTHON_VERSION \
numpy=$NUMPY_VERSION \
pytango=$PYTANGO_VERSION \
sardana=$SARDANA_VERSION \
h5py ipython itango

RUN micromamba install --yes \
pyqtgraph \
matplotlib

ENV PATH=/opt/conda/bin:$PATH

