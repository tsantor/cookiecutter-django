#!/bin/bash
source /home/vagrant/env/bin/activate
cd /home/vagrant/project
./manage.py runserver_plus 0.0.0.0:8000
