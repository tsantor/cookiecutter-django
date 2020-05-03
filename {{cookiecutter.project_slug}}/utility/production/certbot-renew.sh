#!/bin/bash

STOP_NGINX=service nginx stop
START_NGINX=service nginx start
KILL_PORT80=kill `sudo lsof -t -i:80`
KILL_PORT443=kill `sudo lsof -t -i:443`
SUPERVISOR_RESTART_ALL=supervisorctl restart all


certbot renew --pre-hook "${$STOP_NGINX};${KILL_PORT80};${KILL_PORT443}" --post-hook "${KILL_PORT80};${KILL_PORT443};${START_NGINX};${SUPERVISOR_RESTART_ALL}"


# su root
# crontab -e
# every-day-at-1am
# 0 1 * * * sudo certbot renew
