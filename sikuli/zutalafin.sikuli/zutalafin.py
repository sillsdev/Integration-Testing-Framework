from sikuli import *

import a_setup
from test_helper import TestHelper

helper = TestHelper("close_flex")

# Close FLEX - This is the last script
switchApp("FieldWorks Language Explorer")
helper.Click("1436902218392.png", "Cannot find orange close button")

if helper.has_fail():
    helper.write_fail("Failed to close")
helper.write_success()

