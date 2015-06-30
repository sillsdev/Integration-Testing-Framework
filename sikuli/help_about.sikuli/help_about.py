import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from flex_regions import *
from test_helper import TestHelper

helper = TestHelper("help_about")
set_flex_helper(helper)

TOOLBARS.Click("Help.png", "Help button not found")
helper.Click("AboutLanguag.png", "About Language Explorer button not found")
    
helper.Exists("7AboutSILFle.png", "`About` screen didn't pop up")
helper.Click("OK.png", "`About` screen doesn't contain `OK`")

helper.write_success()

