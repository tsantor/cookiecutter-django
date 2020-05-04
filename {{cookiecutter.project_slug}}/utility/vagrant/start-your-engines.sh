#!/bin/bash

# Install requirements:
echo "=> Install requirements ..."
pip install -r requirements/local.txt
pip install -r requirements/production.txt

# Copy the `env.example` file to create your `.env` file:
cp env.example .env

# Migrate the database:
echo "=> Migrate ..."
./manage.py migrate

## Install npm
echo "=> Install npm and packages ..."
sudo apt -y install npm
npm install

echo "=> Create a Superuser ..."
./manage.py createsuperuser

## Run the development server
echo "=> Run the dev server ..."
npm run dev
