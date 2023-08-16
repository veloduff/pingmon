#!/bin/bash

## As of Aug/2023 - dir/file locations are hardcoded for linux/MacOS

## Add this to root's crontab, running every 5 minutes or
##  some time greater than ((7 * $PING_SLEEP_TIME) + $REBOOT_SLEEP_TIME)
##
##  */5 * * * * /path/to/ping-wd.sh
##
## This script pings $HOST 7 times, if it doesn't succeed
##  after 7 attempts a reboot command is run

# Touch this file to disable check
DISABLE_CHECK=/path/to/no-internet-check

FAILED_PING=0
LOG_FILE=/var/log/messages.ping
HOST="8.8.8.8"
STATUS=none
PING_SLEEP_TIME=20


# Check for troublshooing status file
if [[ -f $DISABLE_CHECK ]]
then
  DATE=$(date +"%b %d %T")
  echo "$DATE Ping check is disabled: $DISABLE_CHECK file exists" >> $LOG_FILE
  exit 0
fi

## This checks 7 times with PING_SLEEP_TIME after each check
for i in {1..7}
do
  DATE=$(date +"%b %d %T")
  if /bin/ping -c 1 -W 2 $HOST &> /dev/null
  then
    STATUS=success
  else
    ((FAILED_PING = $FAILED_PING + 1))
    STATUS="failure (${FAILED_PING})"
  fi
  echo "$DATE Ping check on internet: $STATUS" >> $LOG_FILE
  sleep $PING_SLEEP_TIME
done

if [[ $FAILED_PING -gt 4 ]]
then
  REBOOT_SLEEP_TIME=60
  DATE=$(date +"%b %d %T")
  echo "$DATE Internet is down or unstable, failed count: $FAILED_PING" >> $LOG_FILE
  echo "$DATE rebooting in $REBOOT_SLEEP_TIME secs ..." >> $LOG_FILE
  sleep $REBOOT_SLEEP_TIME

  DATE=$(date +"%b %d %T")
  echo "$DATE rebooting ..." >> $LOG_FILE
  /sbin/reboot
fi

exit 0

