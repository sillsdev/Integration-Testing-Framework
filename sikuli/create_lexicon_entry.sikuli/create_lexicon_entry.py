import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from sikuli import *
from logger import Logger
from waiting_wrappers import *
from flex_regions import *
from Regionplus import *

log = Logger("create_lexicon_entry")

try:
    Click("Lexicon.png")
except FindFailed:
    log.write_fail("Couldn't find 'Lexicon' button")

try:
    LEFT_SIDEBAR.Click("EHLexiconEdi.png")
except FindFailed:
    log.write_fail("Couldn't find 'Lexicon Edit' button")

try:
    MID_TOOLBAR.Click("Headword.png")
except FindFailed:
    log.write_fail("Couldn't find Headword button")

try:
    TOOLBARS.Click("1435675185765.png")
except FindFailed:
    log.write_fail("Couldn't find 'Create new lexical entry' button")

Type("cat" + Key.ENTER)

if Region(147,101,537,692).exists("catcat.png") is None:
    log.write_fail("Cannot find new 'cat' entry")

if not log.has_fail():
    log.write("Success")
    