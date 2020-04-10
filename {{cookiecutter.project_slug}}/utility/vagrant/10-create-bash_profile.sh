#!/usr/bin/env bash

touch ~/.bash_profile

echo 'alias app="source ~/env/bin/activate && cd ~/project"' >> ~/.bash_profile
echo 'alias rsp="app && ./manage.py runserver_plus 0.0.0.0:8000"' >> ~/.bash_profile
source ~/.bash_profile
