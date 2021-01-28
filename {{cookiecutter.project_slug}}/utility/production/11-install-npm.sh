#!/usr/bin/env bash

echo '==> Install npm...'
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs

# In order for some npm packages to work (those that require compiling code from source)
sudo apt install build-essential

cd ~/project/
npm install
