#!/bin/bash

# cd to project folder
cd /srv/django_app/app

# activate venv and load all environment variables
source .env

#try to kill old process
pid=`cat gunicorn_pids`
echo "Killing old process with PID = $pid"
kill $pid

# run pre deploy maintenance tasks
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# start the detached gunicorn process per gunicorn_cfg settings via pipenv.
gunicorn -D -p gunicorn_pids -c gunicorn_cfg.py app.wsgi
