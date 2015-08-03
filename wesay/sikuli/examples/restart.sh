#!/bin/bash

#kill `pidof mono`

# Mono isn't full name in this case, grabs full names containing mono
killall `ps cax | grep mono | awk '{print $5}'`

echo "examples/restart_flex.sh"
ps cax | grep mono > /dev/null
if [ $? -eq 0 ]; then
  echo "Process is running."
  #sudo killall mono # kill all mono if more than one ~ Ryan
  killall `ps cax | grep mono | awk '{print $5}'`

else
  echo "Process is not running."
fi
/home/vagrant/Integration-Testing-Framework/scripts/memory_clean.sh

wesay &
#fieldworks-flex &
disown %1
