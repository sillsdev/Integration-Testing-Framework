from sikuli import *
import sys, os, subprocess
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')
from test_helper import TestHelper

open_project_helper = TestHelper("open_flex")

# Handlers for things appearing on-screen
def open_handler(event):
    open_project_helper.write("Successfully opened flex.")
    # Don't stop observer, to give it time to open before
    # the next script runs.

def green_handler(event):
    open_project_helper.write_fail("An error has occurred (green), trying to open existing project")
    event.region.stopObserver()
    #os.system("sudo sh /home/vagrant/linux_setup/flex/flex_restart.sh")
    #subprocess.call(["sudo", "/home/vagrant/linux_setup/flex/flex_restart.sh"], shell=True)
    subprocess.Popen("sudo -u vagrant /home/vagrant/linux_setup/flex/flex_restart.sh")
    open_project_helper.write("Successfully restarted flex.")    

# Open Flex from the start screen
def open_new_project(project_name="hello"):
    
    open_project_helper.Click("Createanewpr.png", "Cannot find `Create a new project`")
    type(project_name)
    open_project_helper.Click("OK.png", "Cannot find `OK`")
    if exists(Pattern("OK-2.png").similar(0.88)):
        open_project_helper.Click(Pattern("OK-1.png").similar(0.86), "Cannot find `OK`")
    else:
        open_project_helper.Click(Pattern("Qpen.png").similar(0.80), "Cannot find `Open`")
        
    onAppear("1435347136957.png", open_handler)
    onAppear(Pattern("Anerrorhasoc.png").similar(0.90), green_handler)
    observe(40)
    
    if open_project_helper.has_fail():
        open_project_helper.write_fail("Failed to open")
