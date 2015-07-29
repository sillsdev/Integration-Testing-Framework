from sikuli import *
import sys
sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples')
from test_helper import TestHelper
from flex_regions import *
from Regionplus import Regionplus

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
        helper.write("'" + word + "' field looks the same as in provided image")
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
    column_menu = Regionplus(helper, column_menu.right())
    if not column_menu.Click(Pattern("1436391324903.png").similar(0.90),
        "Couldn't find arrow for drop-down menu, trying to expand column", give_up=False):
        
        # Click on hopefully a different test, so the view of our text will reset
        helper.Click(Pattern("Show.png").targetOffset(0, 30),
            "Couldn't find 'Show All'", time=3)
        
        # Drag out the column so the arrow is visible
        while not column_menu.exists(Pattern("1436391324903.png").similar(0.90)):
            drag_point = helper.Find(Pattern("1436455824256.png").targetOffset(8,0), "Couldn't find point to drag out column", time=2)
            drop_point = helper.Find(Pattern("Title.png").similar(0.90), "Couldn't find 'Title'")
            dragDrop(drag_point, drop_point)
            
        # Click the arrow
        column_menu.Click(Pattern("1436391324903.png").similar(0.90),
            "Couldn't find arrow for drop-down menu even after expanding column")
        
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
    text_region = Regionplus(helper, text_header.below())
    text_region.Click("PrintView.png", " Couldn't find 'Print View' tab")

    # Goal
    ###############
    if text_region.exists(Pattern(compare_path).similar(0.9)):
        helper.write("'" + text + "' print view looks the same as in provided image")
    else:
        helper.write("'" + text + "' print view has changed")


def check_dictionary(compare_path):

    # Opening
    ################
    helper = TestHelper("check_dictionary_change")
    set_flex_helper(helper)
    
    helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
    # First make sure all entries are showing
    LEFT_SIDEBAR.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button", time=10)
    if not exists(Pattern("ieadwordShow.png").similar(0.90)):
        helper.Click(Pattern("LexemeForm.png").targetOffset(-52,23), "'Lexeme Form' column not found")
        helper.Click(Pattern("Headword-1.png").similar(0.90).targetOffset(0,50), "Couldn't find 'Headword'", time=15)
    
    LEFT_SIDEBAR.Click("ElDictionary.png", "Couldn't find 'Dictionary' button", time=20)

    # Goal
    #################
    TOOLBARS.Click("1436456695019.png", "Couldn't find 'First' button -- may already be at start", give_up=False)
    if exists(Pattern(compare_path).similar(0.9)):
        helper.write("Dictionary looks the same as in provided image")
    else:
        helper.write("Dictionary print view has changed")