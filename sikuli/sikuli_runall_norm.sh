#!/bin/bash
#sleep 6m
#rm -Rf /home/vagrant/.local/share/fieldworks/Projects/hel*
for D in `find /home/vagrant/linux_setup/sikuli/*.sikuli -type d`
do
	echo Running $D ...
	sikuli $D
	rm /home/vagrant/*.png
done
