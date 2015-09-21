#!/bin/bash
#sleep 6m
#rm -Rf /home/vagrant/.local/share/fieldworks/Projects/hel*
for D in `find /home/vagrant/Integration-Testing-Framework/sikuli/*.sikuli -type d`
do
	ps cax | grep mono > /dev/null
	if [ $? -eq 0 ]; then
	  (echo -n `date +"%T"`; echo -n"" `date +"%D"`; echo "" Running $D ...)
	  (echo -n `date +"%T"`; echo -n "" `date +"%D"`;echo "" Running $D ...) >> /vagrant/error_log
          sikuli $D
          rm /home/vagrant/*.png > /dev/null
	else
	  echo "FLEx is not running."
	  echo "FLEx is not running." >> /vagrant/error_log
	  exit #break
	fi
done
