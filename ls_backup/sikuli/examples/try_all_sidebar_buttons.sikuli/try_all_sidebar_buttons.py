import flex_regions
from waiting_wrappers import *

"""
Click through all of the buttons in the left sidebar.
Make sure the middle part of the screen changes
within 5 seconds.
[Currently just has a popup if nothing changed, and exits]
If an information box pops up, close it.
Return to first option when done.
"""

changed = "moon"

def stop_observer(event):
    if Region(148,139,544,545).exists("information_popup.png") != None:
        Type(Key.ENTER)
    else:
        event.region.stopObserver()
        global changed
        changed = True
        popup("changed = " + str(changed))
    

def try_all_sidebar_buttons():
    first_region = Region(21,127,115,15)

    # Set initial region to click
    region = first_region.offset(Location(0, 18))
    count = 0
    # Change image recognition settings
    default_similarity = Settings.MinSimilarity
    Settings.MinSimilarity = 0.99
    
    # keep clicking while the list still has items 
    while region.exists("blank_space.png") == None:
        
        global changed
        changed = False

        # keep count and make sure we don't go too far
        count += 1
        if count > 9:
            popup("script malfunction")
            exit(2)

        # Click in the middle of the region and react to change
        flex_regions.MID_TOOLBAR.onChange(stop_observer)
        Click(region.getCenter())
        flex_regions.MID_TOOLBAR.observe(5)
        popup("changed = " + str(changed))
        # Check if the observer stopped as intended
        if not changed:
            popup("No change when clicking item " + str(count))
            return

        # Move region down by 18 pixels
        region = region.offset(Location(0, 18))

    # go back to default screen + settings
    Click(first_region.getCenter())
    Settings.MinSimilarity = default_similarity


try_all_sidebar_buttons()