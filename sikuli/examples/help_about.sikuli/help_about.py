from flex_regions import *
from waiting_wrappers import *
    

TOOLBARS.Click("Help.png")
Click("AboutLanguag.png")
region = Region(2,2,1232,943)
if region.exists("7AboutSILFle.png") is None:
    f = open("error_log", "a")
    try:
        f.write("about screen didn't pop up\n")
    finally:
        f.close()

