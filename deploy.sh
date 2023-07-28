#!/bin/bash

if [ -z $1 ]; then
  echo "Usage: ./deploy.sh <arch>. Example: ./deploy.sh armv7. Available architectures: armv6, armv7."
  exit 1
fi

cd ansible || exit
ansible-playbook -i production server.yml --tags common,$1
