#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: deploy_ssh_keys.sh <user@ip_address>"
  exit 1
fi

local_file="config/authorized_keys"
remote_user="$1"
remote_directory="/home/pc/.ssh"

# Copy the file to the remote server and create non-existing directories
rsync -av -e ssh --rsync-path="mkdir -p $remote_directory && rsync" "$local_file" "$remote_user":"$remote_directory"/