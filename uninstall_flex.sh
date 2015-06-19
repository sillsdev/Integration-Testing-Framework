#!/bin/bash

# sudo -u root ./uninstall_flex.sh
apt-get -y remove fieldworks-applications
apt-get -y autoremove
apt-get -y autoclean
