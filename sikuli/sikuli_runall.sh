#!/bin/bash
#sleep 6m
for D in `find ./*.sikuli -type d`
do
	echo Running $D ...
	sikuli $D
done
