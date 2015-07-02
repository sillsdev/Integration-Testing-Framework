from sikuli import *
from Regionplus import *

LEFT_SIDEBAR = Regionplus(None, Region(0,99,140,335))
MID_TOOLBAR = Regionplus(None, Region(145,99,670,253))
TOOLBARS = Regionplus(None, Region(5,51,650,51))

def set_flex_helper(test_helper):
    regions = [LEFT_SIDEBAR, MID_TOOLBAR, TOOLBARS]
    for r in regions:
        r.set_helper(test_helper)