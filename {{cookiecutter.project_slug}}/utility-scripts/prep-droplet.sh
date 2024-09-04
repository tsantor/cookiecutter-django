#!/usr/bin/env bash

USERNAME={{cookiecutter.project_user}}

sudo apt install -y make apache2-utils docker-compose

# Docker without sudo
sudo groupadd docker
sudo usermod -aG docker $USERNAME
newgrp docker
