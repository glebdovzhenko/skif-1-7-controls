FROM artefact.skao.int/ska-tango-images-tango-cpp:10.1.2 AS build

RUN <<EOF
apt-get update
apt-get install -y cmake pkg-config
EOF


RUN mkdir -p /usr/src/tango-starter
WORKDIR /usr/src/tango-starter

RUN <<EOF
git clone --recurse-submodules https://gitlab.com/tango-controls/starter.git
mkdir -p starter/build
cd starter/build
cmake ../
make
EOF

#FROM artefact.skao.int/ska-tango-images-tango-base:0.4.1 AS result
FROM artefact.skao.int/ska-tango-images-tango-itango:10.1.4 AS result
COPY --from=build /usr/src/tango-starter/starter/build/Starter /home/tango/Starter
