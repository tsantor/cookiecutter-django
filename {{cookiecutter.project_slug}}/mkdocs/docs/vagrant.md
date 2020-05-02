# Django Vagrant Development

## Step 1
Clone the Django project you wish to work on:

## Step 2
Download django-box-0.1.0.box from [here](#) and place it in the root of the cloned repo.

## Step 3

    vagrant up

## Step 4
Run the following command:

    app

This will put you in a Python 3.8 virtual env and cd into the project root.

## Step 5 - Install npm
Install npm and its packages we'll be using with Gulp.

    sudo apt -y install npm
    npm install

## Step 6 - Run the development server
Run the development server with npm while watchin files (css, js, img) files for changes.

    npm run dev
    # or without autoreload or watching files
    rsp

## Step 7 - Checkout what is out of the box

- http://localhost:8082/ - bootstrapped templates with signup/login.
- http://localhost:8082/admin/ - this is mainly for developers to quickly do certain things, we typically comment it out when in production.
- http://localhost:8082/customadmin/ - this is what we use to develop client facing CMS/admins
