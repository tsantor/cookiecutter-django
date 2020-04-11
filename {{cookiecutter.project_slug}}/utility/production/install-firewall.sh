#!/usr/bin/env bash

echo "=> Install and configure firewall ..."
sudo apt-get -y install ufw
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw deny ftp
sudo ufw enable
sudo ufw status verbose
