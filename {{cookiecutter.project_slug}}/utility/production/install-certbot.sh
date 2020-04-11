#!/bin/bash

# Install certbot
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y python-certbot-nginx

read -p "Install cert? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # Stop nginx, install cert, kill Nginx and restart it
    sudo service nginx stop
    sudo certbot --nginx
    sudo kill `sudo lsof -t -i:80`
    sudo service nginx start
fi
