#!/bin/bash

env=$1
env_file="config/.env.${env}"

if [ ! -f "$env_file" ]; then
  echo "File ${env_file} does not exist."
  exit 1
fi

export $(grep -v "^#" "$env_file" | xargs)