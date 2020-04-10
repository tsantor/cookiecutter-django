#!/usr/bin/env bash

VERSION=3.8.1  # 3.7.6, 3.8.1, etc.

# Pre-reqs
sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev

if ! hash python3.7 &> /dev/null; then
    # Step 1 – Install Required Packages
    sudo apt-get build-dep python3
    sudo apt-get -y install build-essential checkinstall
    sudo apt-get -y install zlib1g-dev

    # Step 2 – Download Python
    mkdir ~/tmp && cd ~/tmp
    sudo wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tgz
    sudo tar xzf Python-$VERSION.tgz

    # Step 3 – Compile Python Source
    cd Python-$VERSION
    sudo ./configure --with-ssl
    sudo make altinstall

    # Step 4 – Check Python Version
    python3.8 -V
else
    echo "Python $VERSION already installed"
fi
