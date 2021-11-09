#!/bin/sh


cd /home/ubuntu/dps_bookstore

python3 web_app/run.py

while : ; do
    echo "start flask server"
    cd /home/ubuntu/dps_bookstore/ && python3 -u web_app/run.py >> web_app/run_log.log 2>&1
done &
