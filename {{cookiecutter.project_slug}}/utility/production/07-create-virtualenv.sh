#!/usr/bin/env bash

USER={{ cookiecutter.project_user }}
PROJECT={{ cookiecutter.project_slug }}

USER_DIR=/home/${USER}
ENV_DIR=${USER_DIR}/${USER}_env
PROJECT_DIR=${USER_DIR}/${PROJECT}

sudo apt-get -y install python-virtualenv
virtualenv ${ENV_DIR} --python=`which python3.8`
source ${ENV_DIR}/bin/activate

cd ${PROJECT_DIR}

pip install -r requirements/local.txt
pip install -r requirements/production.txt
