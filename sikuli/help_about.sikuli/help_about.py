from a_setup import *
from test_helper import TestHelper
from flex_regions import *

# Setup
helper = TestHelper("help_about")
set_flex_helper(helper)

# Opening
#############
TOOLBARS.wait("Help.png",300)
TOOLBARS.Click("Help.png", "Help button not found")
helper.Click("AboutLanguag.png", "About Language Explorer button not found")

# Goal
#############
helper.Exists("7AboutSILFle.png", "`About` screen didn't pop up")

# Closing
#############
helper.Click("OK.png", "`About` screen doesn't contain `OK`", restart=True)

helper.write_success()

