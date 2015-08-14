from a_setup import *
from sikuli import *
from test_helper import TestHelper
from flex_regions import *
from Regionplus import *

# Setup
helper = TestHelper("drag_column")
set_flex_helper(helper)

# Opening
#############
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
LEFT_SIDEBAR.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button")

# Goal
#############

# Not doing the drag-drop directly, so if it fails we can
# pinpoint what wasn't found
glosses = MID_TOOLBAR.Find("3losses.png", "Couldn't find 'Glosses' column header")
target = MID_TOOLBAR.Find("lLexemeJorm_.png",
    "'Headword' and 'Lexeme Form' headers not where expected")
dragDrop(glosses, target)

# Check that it's in the new position
helper.Find(Pattern("hexemeformHe.png").similar(0.80), "'Glosses' column not in new position")

# Closing
##############
helper.write_success()

# Drag it back to previous position
glosses = MID_TOOLBAR.Find("3losses.png", "Couldn't find 'Glosses' column header",
    restart=True)
target = MID_TOOLBAR.Find("LexemeFormIG.png",
    "'Lexeme Form' and 'Grammatical Info' headers not where expected",
    restart=True)
dragDrop(glosses, target)