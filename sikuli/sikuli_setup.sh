#!/bin/bash

apt-get -y install sikuli-ide
apt-get -y install libswing-layout-java
apt-get -y install tesseract-ocr tesseract-ocr-eng
apt-get -y install gnome-panel

rm -r /tmp/sikuli
mkdir -p /tmp/sikuli
ln -s /usr/share/tesseract-ocr/tessdata /tmp/sikuli

echo Setup complete.
