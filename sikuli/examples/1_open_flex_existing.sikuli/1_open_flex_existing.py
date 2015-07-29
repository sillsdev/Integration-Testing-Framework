from sikuli import *
import sys
#sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples')
from test_helper import TestHelper

helper = TestHelper("open_flex")

def open_handler(event):
    event.region.stopObserver()
    helper.write("Successfully opened flex (existing project).")
    wait(10)
    exit(0)

# Open an existing project entitled "hello"
# Used to restart flex if it is broken...
# May want to re-write with a way to choose which project is opened.

helper.Click("Openaproject.png", "'Open a project' button not found")
helper.Click(Pattern("lhello.png").similar(0.90).targetOffset(-39,0), "'hello' project not found on 'Open Project' screen")

helper.Click("ectfromacoll.png",
             "'Open' button not found")

# Check that it opens.
onAppear("1435347136957.png", open_handler)
observe(40)

# If we get here, it failed to open.
helper.write_fail("Failed to open")


