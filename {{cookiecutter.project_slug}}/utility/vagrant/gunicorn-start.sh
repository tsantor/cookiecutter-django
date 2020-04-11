#!/bin/bash
NAME="prang" # Name of the application
DJANGODIR=/home/vagrant/project/ # Django project directory
SOCKFILE=/home/vagrant/project/run/gunicorn.sock # we will communicate using this unix socket
VIRTUAL_ENV=/home/vagrant/env # Virtual env directory
USER=vagrant # the user to run as
GROUP=vagrant # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn (2 * num cores)
DJANGO_SETTINGS_MODULE=config.settings.production # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi # WSGI module name
LOG_LEVEL=error

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ${VIRTUAL_ENV}/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ${VIRTUAL_ENV}/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=$LOG_LEVEL \
  --log-file=-
