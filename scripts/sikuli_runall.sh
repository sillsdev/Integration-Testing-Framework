#!/bin/bash
for D in `find ./*.sikuli -type d`
do
        echo Running $D ...
        sikuli $D
done
