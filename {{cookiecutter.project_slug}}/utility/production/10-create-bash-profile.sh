#!/usr/bin/env bash

touch ~/.bash_profile

echo 'alias app="source ~/{{cookiecutter.project_slug}}_env/bin/activate && cd ~/{{cookiecutter.project_slug}}"' >> ~/.bash_profile
echo 'alias collectstatic="app && ./manage.py collectstatic --settings config.settings.production"' >> ~/.bash_profile
source ~/.bash_profile
