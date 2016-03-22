from test_helper import *

# Opening
#############
TOOLBARS.wait("Help.png",300)
TOOLBARS.click("Help.png")
click("AboutLanguag.png")

# Goal
#############
exists("7AboutSILFle.png")

# Closing
#############
click("OK.png")