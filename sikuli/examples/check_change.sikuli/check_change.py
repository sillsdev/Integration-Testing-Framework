from sikuli import *
import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')
from test_helper import TestHelper
from flex_regions import *
from Regionplus import Regionplus

# Currently sometimes thinks there's a change when there' not. ugh.
def check_word(word, compare_path):
    helper = TestHelper("check_lexicon_entry_change")
    set_flex_helper(helper)
    
    # Opening
    ###############
    helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
    LEFT_SIDEBAR.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button", time=10)
    helper.Click(Pattern("LexemeForm.png").targetOffset(-52,23), "'Lexeme Form' column not found")
    helper.Click("lterfor.png", "'Filter for' button not found")
    paste(word)
    
    # Now the 'Filter for' box is up, so if we can't click something
    # we should restart Flex
    helper.Click(Pattern("W_holeitem.png").targetOffset(-42,0), "'Whole item' option not found", restart=True)
    helper.Click(Pattern("OK-1.png").similar(0.85), "OK button not found", time=10, restart=True)
    # 'Filter for' box is gone now, word should be selected automatically
    
    
    # Create a region inside the 'Entry' panel
    entry_header = helper.Find("9EntryHShowH.png",
        "'Entry' field not found in right panel")
    entry_region = entry_header.below()
    
    # Goal
    ###############
    if entry_region.exists(Pattern(compare_path).similar(0.9)):
        helper.write_fail("'" + word + "' field looks the same as in provided image")
    else:
        helper.write("'" + word + "' field has changed")


def check_text(text, compare_path):
    # Opening
    ###############
    helper = TestHelper("check_text_change")
    set_flex_helper(helper)
    
    helper.Click("TUTextsWord.png", "Couldn't find 'Texts & Words' button")
    LEFT_SIDEBAR.Click("InterlinearT.png", "Couldn't find 'Interlinear Texts' button")
    
    # Find the menu to search for text
    column_menu = helper.Find("Show.png", "Couldn't find 'Show All'")
    column_menu = Regionplus(column_menu.right())
    column_menu.Click(Pattern("1436391324903.png").similar(0.90), "Couldn't find arrow for drop-down menu")
    helper.Click("lterfor.png", "'Filter for' button not found")
    paste(text) 

    # Now the 'Filter for' box is up, so if we can't click something
    # we should restart Flex
    helper.Click(Pattern("W_holeitem.png").targetOffset(-42,0), "'Whole item' option not found", restart=True)
    helper.Click(Pattern("OK-1.png").similar(0.85), "OK button not found", time=10, restart=True)
    # 'Filter for' box is gone now, text should be selected automatically

    # Create a region inside the 'Entry' panel
    text_header = helper.Find("1436391807956.png",
        "'Text' field not found in right panel")
    text_region = Regionplus(text_header.below())
    text_region.Click("PrintView.png", " Couldn't find 'Print View' tab")

    # Goal
    ###############
    if text_region.exists(Pattern(compare_path).similar(0.9)):
        helper.write_fail("'" + text + "' print view looks the same as in provided image")
    else:
        helper.write("'" + text + "' print view has changed")
        