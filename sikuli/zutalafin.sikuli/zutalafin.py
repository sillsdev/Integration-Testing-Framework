from sikuli import *
from test_helper import TestHelper

sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

helper = TestHelper("close_flex")

# Close FLEX - This is the last script
helper.Click("1436902218392.png", "Cannot find orange close button")

if helper.has_fail():
    helper.write_fail("Failed to close")
helper.write_success()

