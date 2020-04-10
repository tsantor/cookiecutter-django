#!/usr/bin/env bash

USER=vagrant
PROJECT=prang_power
TARGET_ENV=vagrant

USER_DIR=/home/${USER}
PROJECT_DIR=${USER_DIR}/${PROJECT}

echo "Copy supervisor.conf..."
# sudo ln -sfv ${PROJECT_DIR}/conf/${TARGET_ENV}/supervisor.conf /etc/supervisord.d/prang_power.conf
sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/supervisor.conf /etc/supervisord.d/prang_power.conf

echo "Restart nginx and supervisor..."
# sudo systemctl restart nginx
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart all
sudo supervisorctl status

# echo "Make the logs dir..."
# mkdir -p ${PROJECT_DIR}/logs
