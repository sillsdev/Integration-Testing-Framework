#!/bin/bash

kill `pidof mono`

ps cax | grep mono > /dev/null
echo "examples/restart_flex.sh"
if [ $? -eq 0 ]; then
  echo "Process is running."
  sudo kill `pidof mono`
else
  echo "Process is not running."
fi

fieldworks-flex &
disown %1
