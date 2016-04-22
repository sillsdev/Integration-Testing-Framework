from sikuli import *
from test_helper import *
import os
def open_handler(event):
    Debug.user("Successfully opened flex.")
    event.stopObserver()
    wait(45)
    # Don't stop observer, to give it time to open before
    # the next script runs.

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
    observe(300)
