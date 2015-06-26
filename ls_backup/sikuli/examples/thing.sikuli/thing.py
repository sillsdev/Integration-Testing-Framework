
toolbar_region = Region(5,51,643,49)
edit_match = toolbar_region.find("Edit-1.png")
click(edit_match)
try:
    click("FindLexicalEntry.png")
except FindFailed:
    click("1435005725038.png")
    
wait(1)
click("Cancel.png")
wait(1)
try:
    click("1435005761097.png")
except FindFailed:
    click("1435005725038.png")
    print "lololol"
    # org.sikuli.script.Region.handleFindFailed
