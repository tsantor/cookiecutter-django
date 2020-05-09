#!/usr/bin/env bash

USER=vagrant
PROJECT=project
TARGET_ENV=vagrant

USER_DIR=/home/${USER}
PROJECT_DIR=${USER_DIR}/${PROJECT}

echo "$(tput setaf 6)=> Copy supervisor.conf ...$(tput sgr0)"
sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/supervisor.conf /etc/supervisor/conf.d/{{ cookiecutter.project_slug }}.conf

echo "$(tput setaf 6)=> Copy nginx.conf ...$(tput sgr0)"
sudo rm /etc/nginx/sites-available/default 2> /dev/null
sudo rm /etc/nginx/sites-enabled/default 2> /dev/null
sudo cp -fv ${PROJECT_DIR}/conf/${TARGET_ENV}/nginx.conf /etc/nginx/sites-available/project.conf
sudo ln -sfv /etc/nginx/sites-available/project.conf /etc/nginx/sites-enabled/project.conf

echo "$(tput setaf 6)=> Restart supervised processes ...$(tput sgr0)"
# sudo service nginx restart
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart all
sudo supervisorctl status

echo -e "$(tput setaf 6)=> Make the logs dir ...$(tput sgr0)"
mkdir -p ${PROJECT_DIR}/logs
