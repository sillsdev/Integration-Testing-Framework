#!/bin/bash
for D in `find /home/vagrant/linux_setup/sikuli/*.sikuli -type d`
do
        echo Running $D ...
        sikuli $D
done
