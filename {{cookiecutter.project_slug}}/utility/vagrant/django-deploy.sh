#!/usr/bin/env bash

USER=vagrant
PROJECT=project
TARGET_ENV=vagrant

USER_DIR=/home/${USER}
PROJECT_DIR=${USER_DIR}/${PROJECT}

echo "Copy supervisor.conf..."
sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.project_slug }}.conf

# echo "Copy nginx.conf..."
# sudo rm /etc/nginx/sites-available/default 2> /dev/null
# sudo rm /etc/nginx/sites-enabled/default 2> /dev/null
# sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/nginx.conf /etc/nginx/sites-available/{{ cookiecutter.project_slug }}.conf
# sudo ln -sfv /etc/nginx/sites-available/{{ cookiecutter.project_slug }}.conf /etc/nginx/sites-enabled/{{ cookiecutter.project_slug }}.conf

echo "Restart supervised services..."
# sudo service nginx restart
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart all
sudo supervisorctl status

echo "Make the logs dir..."
mkdir -p ${PROJECT_DIR}/logs
