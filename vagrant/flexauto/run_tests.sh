#!/bin/bash
export DISPLAY=:0.0

### Change screen resolution
xrandr --output VGA-0 --mode 1024x768

### FieldWorks Sharing
#/usr/lib/fieldworks/ShareFwProjects

### Start Flex
sudo rm -Rf /home/vagrant/.local/share/fieldworks/Projects/*
fieldworks-flex &

### Sikuli XScripts
runsikulix -r /home/vagrant/Integration-Testing-Framework/sikuli_runall.sikuli

exit