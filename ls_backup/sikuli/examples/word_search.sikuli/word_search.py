from sikuli import *
import flex_regions
import waiting_wrappers
import Regionplus
reload(flex_regions)
reload(waiting_wrappers)
reload(Regionplus)
from flex_regions import *
from waiting_wrappers import *
from Regionplus import *

# Click Lexicon Edit: Search for the string "Browse"
# in the left sidebar, and click the location at a 
# (19, -19) offset from what was found.
browse = LEFT_SIDEBAR.find("Browse")
lexedit = Location(browse.getTarget()).offset(19, -19)
Click(lexedit)
try:
    print "hi"
    #MID_TOOLBAR.Click(Pattern("headword.png").targetOffset(53,22))
except FindFailed, ff:
    popup(ff.message)
    exit(1)
    
try:
    MID_TOOLBAR.Click("filter_for.png")
except FindFailed, ff:
    popup(ff.message)
    exit(1)
#MID_TOOLBAR.click("Filter for...")
Type("aka")
type(Key.ENTER)
wait(0.5)

