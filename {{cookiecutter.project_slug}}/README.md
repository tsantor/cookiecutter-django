# {{ cookiecutter.project_name }}

## Create a Development Environment using Vagrant

### Clone the Repo

    git clone https://bitbucket.org/xstudios/{{ cookiecutter.project_slug }}

### Create Env Settings

Create `.env` using `env.example` as a guide.

### Use Vagrant

In order to make our dev environment portable we leverage Vagrant. Obtain the vagrant box from the project lead. Place the box in the root of the project and run:

    # Notify vagrant of file changes
    vagrant plugin install vagrant-notify-forwarder

    vagrant up
    vagrant ssh

Once SSH'd in run:

    app
    npm install
    npm run dev

You can then access the site at `http://localhost:3000/` and the BrowserSync GUI at `http://localhost:3001`
