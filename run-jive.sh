export TANGO_HOST=127.0.0.1:10000
docker run --security-opt label=type:container_runtime_t \
    --net=host --user $(id -u):$(id -g) \
    -e TANGO_HOST=$TANGO_HOST -e DISPLAY=$DISPLAY -e XAUTHORITY="/Xauthority" \
    -v /tmp/.X11-unix:/tmp/.X11-unix:z -v ${XAUTHORITY:-$HOME/.Xauthority}:/Xauthority:ro \
    --rm artefact.skao.int/ska-tango-images-tango-jive:7.45.1
