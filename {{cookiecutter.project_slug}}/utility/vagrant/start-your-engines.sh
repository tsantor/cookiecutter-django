#!/bin/bash

# Install requirements:
echo "$(tput setaf 6)=> Install requirements ...$(tput sgr0)"
pip install -r requirements/local.txt
pip install -r requirements/production.txt

# Copy the `env.example` file to create your `.env` file:
cp env.example .env

# Migrate the database:
echo "$(tput setaf 6)=> Migrate ...$(tput sgr0)"
./manage.py migrate

## Install npm
echo "$(tput setaf 6)=> Install npm and packages ...$(tput sgr0)"
sudo apt -y install npm
npm install

echo "$(tput setaf 6)=> Create a Superuser ...$(tput sgr0)"
./manage.py createsuperuser

## Run the development server
echo "$(tput setaf 6)=> Run the dev server ...$(tput sgr0)"
npm run dev
