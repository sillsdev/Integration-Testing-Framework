from sikuli import *
from test_helper import *
import os


# Handlers for things appearing on-screen
def open_handler(event):
    Debug.user("Successfully opened flex.")
    stopObserver()
    wait(45)
    # Don't stop observer, to give it time to open before
    # the next script runs.

def green_handler(event):
    Debug.user("An error has occurred (green), trying to open existing project")
    event.region.stopObserver()
    #os.system(". /home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh")
    #subprocess.call(["sudo", "/home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh"], shell=True)
    #subprocess.Popen("sudo -u vagrant /home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh")
    if myOS == OS.LINUX:
        os.system("sudo /home/vagrant/Integration-Testing-Framework/scripts/memory_clean.sh")
    else:
        popup("Only able to recover from green screen on Linux!")
        Debug.user("Only able to recover from green screen on Linux!")
        exit(1)
    Debug.user("Successfully restarted flex.")

# Open Flex from the start screen
def open_new_project(project_name="hello"):

    wait("Createanewpr.png", 300)
    click("Createanewpr.png")
    type(project_name)
    click("OK.png")
    if exists(Pattern("OK-2.png").similar(0.88)):
        click(Pattern("OK-1.png").similar(0.86))
    else:
        click(Pattern("Qpen.png").similar(0.80))
        
    onAppear("1435347136957.png", open_handler)
    onAppear(Pattern("Anerrorhasoc.png").similar(0.90), green_handler)
    observe(300)