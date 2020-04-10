#!/usr/bin/env bash

# Update
sudo apt-get update
sudo apt-get -y upgrade

# Install basic tools
sudo apt-get -y install bash
sudo apt-get -y install build-essential
sudo apt-get -y install cmake
sudo apt-get -y install coreutils
sudo apt-get -y install curl
sudo apt-get -y install git
sudo apt-get -y install grep
sudo apt-get -y install htop
sudo apt-get -y install nano
sudo apt-get -y install nmap
sudo apt-get -y install openssh-server
sudo apt-get -y install openssl
sudo apt-get -y install rsync
sudo apt-get -y install wget
sudo apt-get -y install whois

# Required to translate
sudo apt-get install -y gettext

# Setup firewall
# sudo apt-get -y install ufw
# sudo ufw allow ssh
# sudo ufw allow http
# sudo ufw allow https
# sudo ufw deny ftp
# sudo ufw enable
# sudo ufw status verbose

# Needed for cryptography
# sudo apt-get -y install libffi-dev
# sudo apt-get -y install libssl-dev

# Python3 dev
sudo apt-get install -y python3-dev python3-setuptools

# Install virtualenv
sudo apt-get -y install python-virtualenv

# Postgresql and psycopg2 dependencies
sudo apt-get -y install libpq-dev

# Install prerequisites for pillow
sudo apt-get -y install libtiff5-dev
sudo apt-get -y install libjpeg8-dev
sudo apt-get -y install libfreetype6-dev
sudo apt-get -y install liblcms2-dev
sudo apt-get -y install libwebp-dev

# django-extensions
sudo apt-get -y install libgraphviz-dev

# -----------------------------------------------------------------------------
# Project specific commands

