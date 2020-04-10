#!/usr/bin/env bash

sudo apt-get -y install python-virtualenv
cd ~
virtualenv ~/env --python=`which python3.8`
source ~/env/bin/activate

ln -sfv /vagrant ~/project
cd ~/project

pip install -r requirements/local.txt
pip install -r requirements/production.txt
