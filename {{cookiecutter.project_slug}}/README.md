# {{ cookiecutter.project_name }}

## Create a Development Environment using Vagrant

### Clone the Repo

    git clone https://bitbucket.org/xstudios/{{ cookiecutter.project_slug }}

### First Run Only
In order to make our dev environment portable we leverage Vagrant. Obtain the vagrant box from the project lead. Place the box in the root of the project and run:

    # Notify vagrant of file changes
    vagrant plugin install vagrant-notify-forwarder

    vagrant up
    vagrant ssh

Once SSH'd in run:

    app
    ./utility/vagrant/start-your-engines.sh

You can then access the site at `http://localhost:3000/` and the BrowserSync GUI at `http://localhost:3001`. Other URLs of note:

- `http:://localhost:3000/admin/` - Django Admin
- `http:://localhost:3000/customadmin/` - Custom Admin built using Inspinia theme that we use for client facing CMS/Admins.
- `http:://localhost:3000/api/v1/swagger/` - Swagger API

### Subsequent Runs

    vagrant up
    app
    npm run dev
    # or
    rsp


## Tech Stack

- Ubuntu 18.04 LTS
- Django 3
- Python 3.8
- Nginx
- Gunicorn
- PostgreSQL
- Redis
- Celery
- Supervisor
