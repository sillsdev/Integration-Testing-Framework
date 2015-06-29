import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from flex_regions import *
from waiting_wrappers import *
from logger import Logger

log = Logger("help_about")
try:
    TOOLBARS.Click("Help.png")
except FindFailed:
    log.write_fail("Help button not found")

try:
    Click("AboutLanguag.png")
except FindFailed:
    log.write_fail("About Language Explorer button not found")
    
region = Region(2,2,1232,943)
if region.exists("7AboutSILFle.png") is None:
    log.write_fail("`About` screen didn't pop up")
try:
    Click("OK.png")
except FindFailed:
    log.write_fail("`About` screen doesn't contain `OK`")

if not log.has_fail():
    log.write("Success")

