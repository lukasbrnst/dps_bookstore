#!/bin/sh

source $HOME/.bashrc

while : ; do
    echo "start flask server"
    cd /home/ubuntu/dps_bookstore/ && python3 -u web_app/run.py >> web_app/run_log.log 2>&1
    sleep 5
done &
