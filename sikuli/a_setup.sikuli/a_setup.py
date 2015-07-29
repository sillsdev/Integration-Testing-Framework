from sikuli import *
import os
import sys

# Get the folder right above the script's folder.
# (aka the sikuli folder, with all the tests.)
myOS = Env.getOS()
if myOS == OS.LINUX:
    wd = os.path.dirname(getBundlePath())
elif myOS == OS.WINDOWS:
    wd = os.path.dirname(os.path.dirname(getBundlePath()))
else:
    print "Unsupported OS."
    exit(1)

# Put the examples directory in sys.path.
if (wd + "/examples") not in sys.path:
    sys.path.append(wd + "/examples")