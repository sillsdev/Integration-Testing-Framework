from sikuli import *
from test_helper import *
import os

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