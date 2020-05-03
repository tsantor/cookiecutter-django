#!/bin/bash

# Install requirements:
pip install -r requirements/local.txt
pip install -r requirements/production.txt

# Copy the `env.example` file to create your `.env` file:
cp env.example .env

# Migrate the database:
./manage.py migrate
./manage.py createsuperuser

## Install npm
sudo apt -y install npm
npm install

## Run the development server
npm run dev
