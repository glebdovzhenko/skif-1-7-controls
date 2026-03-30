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

 #pytango 9.5.1   py310h9528bbc_0     (+  7 builds) conda-forge linux-64
 #pytango 9.5.0   py310h9528bbc_2     (+ 10 builds) conda-forge linux-64
 #pytango 9.4.2   py310hcfe0b05_1     (+  5 builds) conda-forge linux-64
 #pytango 9.4.1   py310h780ab8f_0     (+ 11 builds) conda-forge linux-64
 #pytango 9.4.0   py310h780ab8f_0     (+  3 builds) conda-forge linux-64
 #pytango 9.3.6   py310h150de76_2     (+ 15 builds) conda-forge linux-64
 #pytango 9.3.5   py310h0c06107_1     (+  7 builds) conda-forge linux-64
 #pytango 9.3.4   py310hb0dbb4a_0     (+  3 builds) conda-forge linux-64
 #pytango 9.3.3   py310h524d31d_2     (+ 14 builds) conda-forge linux-64
 #pytango 10.1.4  np2py310h99cdc5b_0  (+  4 builds) conda-forge linux-64
 #pytango 10.1.3  np2py310h99cdc5b_0  (+  4 builds) conda-forge linux-64
 #pytango 10.1.2  np2py310h99cdc5b_0  (+  4 builds) conda-forge linux-64
 #pytango 10.1.1  np2py310h99cdc5b_0  (+  4 builds) conda-forge linux-64
 #pytango 10.1.0  np2py310h99cdc5b_0  (+  4 builds) conda-forge linux-64
 #pytango 10.0.4  np22py310h1e2e62b_0 (+  3 builds) conda-forge linux-64
 #pytango 10.0.3  np22py310h1e2e62b_1 (+  8 builds) conda-forge linux-64
 #pytango 10.0.2  np22py310h27ac255_2 (+ 13 builds) conda-forge linux-64
 #pytango 10.0.0  py310h52a289b_0     (+  8 builds) conda-forge linux-64

ARG PYTHON_VERSION=3.12
ARG PYTANGO_VERSION=9.5.0
ARG SARDANA_VERSION=3.6.0

RUN micromamba install --yes \
python=$PYTHON_VERSION \
pytango=$PYTANGO_VERSION \
sardana=$SARDANA_VERSION \
h5py ipython itango

RUN micromamba install --yes \
pyqtgraph \
matplotlib

ENV PATH=/opt/conda/bin:$PATH

