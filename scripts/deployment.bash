#!/bin/bash

# if gunicorn_PID.txt
# then
#     pid = `cat gunicorn_PID.txt`
#     echo "Killing old process with PID = $pid"
#     kill $pid
# fi

# start the detached gunicorn process per gunicorn_cfg settings via pipenv.
cd /srv/django_app/app
pipenv run gunicorn -D -c gunicorn_cfg.py app.wsgi

# echo $! > gunicorn_PID.txt
# echo "Started gunicorn server with PID = " $!