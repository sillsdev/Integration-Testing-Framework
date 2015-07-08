#!/bin/bash
sudo kill `pidof mono`

ps cax | grep mono > /dev/null

if [ $? -eq 0 ]; then
  echo "Process is running.\n"
  sudo kill `pidof mono`
else
  echo "Process is not running.\n"
fi
(fieldworks-flex &)
sikuli ~/linux_setup/sikuli/examples/1_open_flex_existing.sikuli &

