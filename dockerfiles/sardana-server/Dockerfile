FROM ubuntu:resolute-20260108

RUN <<EOF
apt-get clean 
apt-get update 
apt-get upgrade -y
EOF

RUN <<EOF
apt-get install -y openjdk-8-jdk zlib1g-dev libomniorb4-dev libcos4-dev omniidl libzmq3-dev 
EOF

RUN <<EOF
apt-get install -y python3 python3-pip python3-venv
EOF

RUN useradd -ms /bin/bash tango 
USER tango
WORKDIR /home/tango

RUN <<EOF
python3 -m venv pytango-env
/home/tango/pytango-env/bin/pip3 install h5py
/home/tango/pytango-env/bin/pip3 install pytango
/home/tango/pytango-env/bin/pip3 install sardana
/home/tango/pytango-env/bin/pip3 install ipython
/home/tango/pytango-env/bin/pip3 install itango
EOF

RUN <<EOF
python3 -m venv pytango-env
/home/tango/pytango-env/bin/pip3 install six
/home/tango/pytango-env/bin/pip3 install newportxps
/home/tango/pytango-env/bin/pip3 install pyvisa
EOF
