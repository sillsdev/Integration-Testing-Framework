from test_helper import *

# Opening
#############
wait("Lexicon.png", 300)
click("Lexicon.png")
LEFT_SIDEBAR.click("LexiconEdit.png")

# Goal
#############

# Not doing the drag-drop directly, so if it fails we can
# pinpoint what wasn't found
glosses = MID_TOOLBAR.find("3losses.png")
target = MID_TOOLBAR.find("lLexemeJorm_.png")
dragDrop(glosses, target)

# Check that it's in the new position
find(Pattern("hexemeformHe.png").similar(0.80))


# Drag it back to previous position
glosses = MID_TOOLBAR.find("3losses.png")
target = MID_TOOLBAR.find("LexemeFormIG.png")
dragDrop(glosses, target)