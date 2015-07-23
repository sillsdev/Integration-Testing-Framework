#!/bin/bash

kill `pidof mono`

ps cax | grep mono > /dev/null
echo "examples/restart_flex.sh"
if [ $? -eq 0 ]; then
  echo "Process is running."
  sudo killall mono # kill all mono if more than one ~ Ryan
else
  echo "Process is not running."
fi

fieldworks-flex &
disown %1
