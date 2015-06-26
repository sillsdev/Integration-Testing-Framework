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
    write_log("Help button not found")
    print "1"

try:
    Click("AboutLanguag.png")
except FindFailed:
    write_log("About Language Explorer button not found")
    print "2"
    
region = Region(2,2,1232,943)
if region.exists("7AboutSILFle.png") is None:
    write_log("about screen didn't pop up")

