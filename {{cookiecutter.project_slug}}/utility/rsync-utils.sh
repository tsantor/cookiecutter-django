#!/usr/bin/env bash

rsync -avzp . {{ cookiecutter.project_user }}@IP:~/utility/ --delete
