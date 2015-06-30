import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

from sikuli import *
from test_helper import TestHelper
from flex_regions import *
from Regionplus import *

helper = TestHelper("create_new_text")
set_flex_helper(helper)

helper.Click("OTextsWord.png", "Couldn't find 'Texts & Words' button")
LEFT_SIDEBAR.Click("InterlinearT.png", "Couldn't find 'Interlinear Texts' button")
TOOLBARS.Click(Pattern("1435693467339.png").similar(0.90), "Couldn't find 'Add new text' button")
helper.Click(Pattern("TitleIFreEng.png").targetOffset(48,-18), "Couldn't find Title field")
helper.Type("Bonjour")
helper.Click(Pattern("TitleIFreEng.png").targetOffset(48,9), "Couldn't find Title field")
helper.Type("Hello" + Key.TAB)
helper.Type("asdf zxcv werdtfyguuio")

Regionplus(helper, Region(147,101,537,692)).Exists("Bonjour.png",
    "Cannot find new 'Bonjour' text")

helper.write_success()