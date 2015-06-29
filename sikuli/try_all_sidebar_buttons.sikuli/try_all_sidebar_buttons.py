import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from sikuli import *
import flex_regions
from logger import Logger

"""
Click through all of the buttons in the left sidebar.
Make sure the middle part of the screen changes
within 5 seconds.
[Currently just has a popup if nothing changed, and exits]
If an information box pops up, close it.
Return to first option when done.
"""

changed = False

def stop_observer(event):
    global changed
    if Region(148,139,544,545).exists("information_popup.png") is not None:
        type(Key.ENTER)
    else:
        event.region.stopObserver()
        changed = True
    

def try_all_sidebar_buttons():
    log = Logger("try_all_side_bar_buttons")
    
    first_region = Region(21,127,115,15)

    # Set initial region to click
    region = first_region.offset(Location(0, 18))
    count = 0
    
    # keep clicking while the list still has items 
    while region.exists(Pattern("blank_space.png").similar(0.99)) == None:
        
        global changed
        changed = False

        # keep count and make sure we don't go too far
        count += 1
        if count > 9:
            log.write_fail("Script malfunction: went too far down the left column")
            break;

        # Click in the middle of the region and react to change
        flex_regions.MID_TOOLBAR.onChange(stop_observer)
        click(region.getCenter())
        flex_regions.MID_TOOLBAR.observe(5)
        # Check if the observer stopped as intended
        if not changed:
            log.write_fail("No change when clicking item " + str(count))

        # Move region down by 18 pixels
        region = region.offset(Location(0, 18))

    # go back to first screen
    click(first_region.getCenter())

    if not log.has_fail():
        log.write("Success")


try_all_sidebar_buttons()