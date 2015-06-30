import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from sikuli import *
from test_helper import TestHelper
from flex_regions import *
from Regionplus import *

# Set up helper
helper = TestHelper("create_notebook_entry")
set_flex_helper(helper)

# Opening
##############
helper.Click("Notebook5.png", "Couldn't find 'Notebook' button", quit=True)
LEFT_SIDEBAR.Click("RecordEdit.png", "Couldn't find 'Record Edit' button", quit=True)
TOOLBARS.Click(Pattern("1435614864882.png").similar(0.96), "Couldn't find 'Create new record' button", quit=True)

# Goal
##############
helper.Type("hello world" + Key.ENTER)

Regionplus(helper, Region(147,101,537,692)).Exists("helloworld.png",
        "Cannot find new 'hello world' entry")

helper.write_success()

# Closing
##############
# (None)
