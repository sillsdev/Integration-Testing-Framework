# Does some path manipulation and imports
# that every test script needs.
# DO NOT move this to different folder from
# the main test scripts: they need to be able
# to find it without editing sys.path.
# Starts with an 'a' because apparently imports
# happen in alphabetical order.

# Note: Can be used in helper scripts, but
# if that helper is **run** directly, and not from a
# main test script, the imports won't work properly.


from sikuli import *
import os
import sys

# Get the folder right above the script's folder.
# (aka the sikuli folder, with all the tests.)
myOS = Env.getOS()
if myOS == OS.LINUX:
    wd = os.path.dirname(getBundlePath())
    # addImagePath(/* linux image directory */)
elif myOS == OS.WINDOWS:
    wd = os.path.dirname(os.path.dirname(getBundlePath()))
    # addImagePath(/* windows image directory */)
else:
    print "Unsupported OS."
    exit(1)

# Put the examples directory in sys.path.
if (wd + "/examples") not in sys.path:
    sys.path.append(wd + "/examples")