#!/usr/bin/env bash

USER=vagrant
DB=project

read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # Drop and create db
    sudo -i -u postgres dropdb $DB
    sudo -i -u postgres createuser $USER -P
    sudo -i -u postgres createdb $DB -O $USER
fi
