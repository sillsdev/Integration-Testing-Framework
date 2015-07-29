#!/bin/bash
for D in `find /home/vagrant/Integration-Testing-Framework/sikuli/*.sikuli -type d`
do
        echo Running $D ...
        sikuli $D
done
