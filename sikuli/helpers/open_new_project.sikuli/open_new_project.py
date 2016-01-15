from sikuli import *
import os
from test_helper import TestHelper

open_project_helper = TestHelper("open_flex")

# Handlers for things appearing on-screen
def open_handler(event):
    open_project_helper.write("Successfully opened flex.")
    stopObserver()
    wait(45)
    # Don't stop observer, to give it time to open before
    # the next script runs.

def green_handler(event):
    open_project_helper.write_fail("An error has occurred (green), trying to open existing project")
    event.region.stopObserver()
    #os.system(". /home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh")
    #subprocess.call(["sudo", "/home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh"], shell=True)
    #subprocess.Popen("sudo -u vagrant /home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh")
    if Env.getOS() == OS.LINUX:
        os.system("sudo /home/vagrant/Integration-Testing-Framework/scripts/memory_clean.sh")
    else:
        popup("Only able to recover from green screen on Linux!")
        helper.write_fail("Only able to recover from green screen on Linux!")
        exit(1)
    open_project_helper.restart_flex()
    open_project_helper.write("Successfully restarted flex.")  

# Open Flex from the start screen
def open_new_project(project_name="hello"):

    wait("Createanewpr.png", 300)
    open_project_helper.Click("Createanewpr.png", "Cannot find `Create a new project`")
    type(project_name)
    open_project_helper.Click("OK.png", "Cannot find `OK`")
    if exists(Pattern("OK-2.png").similar(0.88)):
        open_project_helper.Click(Pattern("OK-1.png").similar(0.86), "Cannot find `OK`")
    else:
        open_project_helper.Click(Pattern("Qpen.png").similar(0.80), "Cannot find `Open`")
        
    onAppear("1435347136957.png", open_handler)
    onAppear(Pattern("Anerrorhasoc.png").similar(0.90), green_handler)
    observe(300)
    
    if open_project_helper.has_fail():
        open_project_helper.write_fail("Failed to open")
