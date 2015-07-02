import sys, os
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')
from waiting_wrappers import *
from logger import Logger

log = Logger("open_flex")
try:
    click("Createanewpr.png")
    wait(1)
except FindFailed:
    log.write("Cannot find `Create a new project`")

type("hello")
try:
    click("OK.png")
    wait(1)
except FindFailed:
    log.write("Cannot find `OK`")
if exists(Pattern("OK-2.png").similar(0.88)):
    try:
        click(Pattern("OK-1.png").similar(0.86))
        wait(1)
    except FindFailed:
        log.write("Cannot find `OK`")
else:
    try:
        click(Pattern("Qpen.png").similar(0.80))
        wait(1)
    except FindFailed:
        log.write("Cannot find `Open`")
def openHandler(event):
    log.write("Successfully opened flex.")
    exit(0)
    
opened = onAppear("1435347136957.png", openHandler)
observe(40)

log.write("open_flex: failed to open")
if exists("Anerrorhasoc.png"):
    log.write("An error has occurred (green)")
    os.system("sudo ./flex_restart.sh")
    #subprocess.call(['./flex_restart.sh'])
    


