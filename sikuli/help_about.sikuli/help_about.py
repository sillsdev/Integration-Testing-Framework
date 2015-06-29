import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from flex_regions import *
from waiting_wrappers import *

def write_log(line):
    f = open("/vagrant/error_log", "a+")
    try:
        f.write(line + "\n")
    finally:
        f.close()
   
try:
    TOOLBARS.Click("Help.png")
except FindFailed:
    write_log("help_about: Help button not found")

try:
    Click("AboutLanguag.png")
except FindFailed:
    write_log("help_about: About Language Explorer button not found")
    
region = Region(2,2,1232,943)
if region.exists("7AboutSILFle.png") is None:
    write_log("help_about: `About` screen didn't pop up")
try:
    Click("OK.png")
except FindFailed:
    write_log("help_about: `About` screen doesn't contain `OK`")

