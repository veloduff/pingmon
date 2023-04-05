#!/bin/bash

## Add this to crontab, running every 5 minutes
##  */5 * * * * /path/to/ping-wd.sh

FAILED_PING=0
LOG_FILE=/var/log/messages
HOST=8.8.8.8
STATUS=none
SLEEP_TIME=20
DISABLE_CHECK=/path/to/no-internet-check

# Check for troublshooing status file
if [[ -f $DISABLE_CHECK ]]
then
  DATE=$(date +"%b %d %T")
  echo "$DATE Ping check is disabled: $DISABLE_CHECK file exists" >> $LOG_FILE
  exit 0
fi

## This checks 7 times with SLEEP_TIME after each check
for i in {1..7}
do
  DATE=$(date +"%b %d %T")
  if /bin/ping -c 1 -W 2 $HOST &> /dev/null
  then
    STATUS=success
  else
    STATUS=failure
    ((FAILED_PING = $FAILED_PING + 1))
  fi
  echo "$DATE Ping check on internet: $STATUS" >> $LOG_FILE
  sleep $SLEEP_TIME
done

if [[ $FAILED_PING -gt 4 ]]
then
  SLEEP_TIME=60
  DATE=$(date +"%b %d %T")
  echo "$DATE Internet is down or unstable, failed count: $FAILED_PING" >> $LOG_FILE
  echo "$DATE rebooting in $SLEEP_TIME secs ..." >> $LOG_FILE
  sleep $SLEEP_TIME

  DATE=$(date +"%b %d %T")
  echo "$DATE rebooting ..." >> $LOG_FILE
  /sbin/reboot
fi

