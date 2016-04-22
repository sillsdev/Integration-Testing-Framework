from sikuli import *
from test_helper import *

def open_handler(event):
    event.region.stopObserver()
    Debug.user("Successfully opened flex (existing project).")
    wait(300)
    exit(0)

# Open an existing project entitled "hello"
# Used to restart flex if it is broken...
# May want to re-write with a way to choose which project is opened.

wait("Openaproject.png", 300)
click("Openaproject.png")
click(Pattern("lhello.png").similar(0.90).targetOffset(-39,0))
click("ectfromacoll.png")

# Check that it opens.
onAppear("1435347136957.png", open_handler)
observe(300)

