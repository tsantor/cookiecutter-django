# Django Vagrant Development

To make development more portable and ensure we're all working in the same environment we use Vagrant to run our development environment.  It runs Ubuntu, same as the production environment.

## Step 1 - Clone the Repo
Clone the Django project you wish to work on:

    git clone https://bitbucket.org/xstudios/{{ cookiecuter.project_slug }}

## Step 2 - Download the Vagrant Box
Download the [django-box-0.1.0.box](#) and place it in the root of the cloned repo.

## Step 3 - Vagrant Up

    vagrant up

## Step 4 - Virtual Env
This following alias will put you in a Python 3.8 virtual env and cd into the project root.

    app

## Step 5 - Install Requireements
Install requirements:

    pip install -r requirements/local.txt
    pip install -r requirements/production.txt

## Step 7
Copy the `env.example` file to create your `.env` file:

    cp env.example .env

## Step 7
Migrate the database:

    ./manage.py migrate
    ./manage.py createsuperuser

## Step 8 - Install npm
Install npm and its packages we'll be using with Gulp.

    sudo apt -y install npm
    npm install

## Step 9 - Run the development server
Run the development server with npm while watchin files (css, js, img) files for changes.

    npm run dev
    # or without autoreload or watching files
    rsp

## Step 10 - Checkout what is out of the box

- http://localhost:8082/ - bootstrapped templates with signup/login.
- http://localhost:8082/admin/ - this is mainly for developers to quickly do certain things, we typically comment it out when in production.
- http://localhost:8082/customadmin/ - this is what we use to develop client facing CMS/admins
