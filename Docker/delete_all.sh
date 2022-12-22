# !/bin/bash

docker ps -aq | xargs docker rm -f
docker images -aq | xargs docker rmi -f
docker network rm flask-network
