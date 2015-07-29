#!/bin/bash
#sudo kill `pidof mono`
killall mono &> /dev/null

ps cax | grep mono > /dev/null
if [ $? -eq 0 ]; then
  echo "Process is running."
  #sudo kill -9 `pidof mono`
  killall -9 mono &> /dev/null
else
  echo "Process is not running."
fi
(fieldworks-flex &)

sikuli ~/Integration-Testing-Framework/sikuli/examples/1_open_flex_existing.sikuli
echo "Sikuli ran " $?
#sleep 20 # with & one line up?

