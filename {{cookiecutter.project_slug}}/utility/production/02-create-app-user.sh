#!/usr/bin/env bash

# Create app user
echo "Create app user ..."
sudo adduser {{ cookiecutter.project_user }}
sudo usermod -aG sudo {{ cookiecutter.project_user }}
sudo usermod -aG www-data {{ cookiecutter.project_user }}

# Allow SSH login for new user
echo "Allow SSH login for new user ..."
mkdir -p /home/{{ cookiecutter.project_user }}/.ssh
touch /home/{{ cookiecutter.project_user }}/.ssh/authorized_keys

chmod 700 /home/{{ cookiecutter.project_user }}/.ssh
chmod 644 /home/{{ cookiecutter.project_user }}/.ssh/authorized_keys

chown -R {{ cookiecutter.project_user }}:{{ cookiecutter.project_user }} /home/{{ cookiecutter.project_user }}/.ssh

echo "Don't forget to add your public key to authorized_keys:"
echo "    cat ~/.ssh/id_rsa.pub"
