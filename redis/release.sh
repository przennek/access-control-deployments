#!/bin/bash

if [ -z $1 ]; then
  echo "Usage ./release.sh <version_tag>"
fi

docker buildx build --platform linux/arm/v7 -t przennek/aca-redis:$1 --push .
