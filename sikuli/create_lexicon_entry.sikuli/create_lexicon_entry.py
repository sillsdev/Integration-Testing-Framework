from a_setup import *

from sikuli import *
from test_helper import TestHelper
from flex_regions import *
from Regionplus import *

# Setup
helper = TestHelper("create_lexicon_entry")
set_flex_helper(helper)

# Opening
#############
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
LEFT_SIDEBAR.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button")
MID_TOOLBAR.Click("Headword.png", "Couldn't find Headword button")
TOOLBARS.Click("1435675185765.png", "Couldn't find 'Create new lexical entry' button")

# Goal
#############
helper.Type("cat" + Key.ENTER)

Regionplus(helper, Region(147,101,537,692)).Exists("catcat.png",
    "Cannot find new 'cat' entry")

# Closing
##############
helper.write_success()
