#!/bin/bash
for D in `find /home/vagrant/sikuli/*.sikuli -type d`
do
        echo Running $D ...
        sikuli $D
done
