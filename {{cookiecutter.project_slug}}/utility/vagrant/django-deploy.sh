#!/usr/bin/env bash

USER=vagrant
PROJECT=project
TARGET_ENV=vagrant

USER_DIR=/home/${USER}
PROJECT_DIR=${USER_DIR}/${PROJECT}

echo "Copy supervisor.conf..."
sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/supervisor.conf /etc/supervisord.d/project.conf

echo "Copy nginx.conf..."
sudo mkdir -p /etc/nginx/conf.d
sudo rm /etc/nginx/conf.d/default.conf
sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/nginx.conf /etc/nginx/conf.d/project.conf

echo "Restart nginx and supervisor..."
sudo systemctl restart nginx
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart all
sudo supervisorctl status

echo "Make the logs dir..."
mkdir -p ${PROJECT_DIR}/logs
