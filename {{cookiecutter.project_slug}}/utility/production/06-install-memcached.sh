#!/bin/bash

# https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-memcached-on-ubuntu-16-04

echo "=> Installing Memcached..."
sudo apt-get update
sudo apt-get -y install memcached
sudo apt-get -y install libmemcached-tools
