#!/bin/bash

kill `pidof mono`

ps cax | grep mono > /dev/null

if [ $? -eq 0 ]; then
  echo "Process is running.\n"
  sudo kill `pidof mono`
else
  echo "Process is not running.\n"
fi

fieldworks-flex &
disown %1
