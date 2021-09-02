#!/usr/bin/env bash

# You should run this as root

USERNAME={{cookiecutter.project_user}}

# Create app user
echo "Create app user ..."
sudo adduser $USERNAME
sudo usermod -aG sudo $USERNAME

# Allow SSH login for new user
echo "Allow SSH login for new user ..."
mkdir -p /home/$USERNAME/.ssh
touch /home/$USERNAME/.ssh/authorized_keys

chmod 700 /home/$USERNAME/.ssh
chmod 644 /home/$USERNAME/.ssh/authorized_keys

cp ~/.ssh/authorized_keys /home/$USERNAME/.ssh/authorized_keys

chown -R $USERNAME:$USERNAME /home/$USERNAME/.ssh
