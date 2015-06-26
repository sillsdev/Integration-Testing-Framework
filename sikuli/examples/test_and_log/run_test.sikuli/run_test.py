from __future__ import with_statement
from sikuli import *
from test_fail import TestFail
from try_all_sidebar_buttons import *

log = TestFail("/vagrant/sikuli_log/")
screen = Screen()

wrong = try_all_sidebar_buttons()
if wrong != 0:
    clicked_region = Region(1,125,134,16).offset(Location(0, wrong * 18))
    clicked = screen.capture(clicked_region.getX(), clicked_region.getY(),
            clicked_region.getW(), clicked_region.getH())
    screenshot = screen.capture(screen.getBounds())
    log.clicked_fail(clicked, screencap=screenshot)