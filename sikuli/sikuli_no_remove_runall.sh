#!/bin/bash
#sleep 6m
#rm -Rf /home/vagrant/.local/share/fieldworks/Projects/hel*
for D in `find /home/vagrant/Integration-Testing-Framework/sikuli/*.sikuli -type d`
do
	ps cax | grep mono > /dev/null
	if [ $? -eq 0 ]; then
	  echo Running $D ...
          sikuli $D
          rm /home/vagrant/*.png > /dev/null
	else
	  echo "FLEX is not running."
	  exit #break
	fi
done
