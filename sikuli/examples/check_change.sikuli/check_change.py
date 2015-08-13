from sikuli import *
from test_helper import TestHelper
from flex_regions import *
from Regionplus import Regionplus

def check_word(word, compare_path):
    helper = TestHelper("check_lexicon_entry_change")
    set_flex_helper(helper)
    
    # Opening
    ###############
    helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button", restart=True)
    LEFT_SIDEBAR.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button", time=10, restart=True)
    helper.Click(Pattern("LexemeForm.png").targetOffset(-52,23), "'Lexeme Form' column not found", restart=True)
    helper.Click("lterfor.png", "'Filter for' button not found", restart=True)
    paste(word)
    
    # Now the 'Filter for' box is up, so if we can't click something
    # we should restart Flex
    helper.Click(Pattern("W_holeitem.png").targetOffset(-42,0), "'Whole item' option not found", restart=True)
    helper.Click(Pattern("OK-1.png").similar(0.85), "OK button not found", time=10, restart=True)
    # 'Filter for' box is gone now, word should be selected automatically
    
    
    # Create a region inside the 'Entry' panel
    entry_header = helper.Find("9Entry.png",
        "'Entry' field not found in right panel", restart=True) 
    below_region = entry_header.below()
    right_region = entry_header.right()
    entry_region = Region(below_region.getX(), below_region.getY(),
                          below_region.getW() + right_region.getW(),
                          below_region.getH())
    
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
    
    helper.Click("TUTextsWord.png", "Couldn't find 'Texts & Words' button", restart=True)
    LEFT_SIDEBAR.Click("InterlinearT.png", "Couldn't find 'Interlinear Texts' button", restart=True)
    
    # Find the menu to search for text
    column_menu = helper.Find("Show.png", "Couldn't find 'Show All'", restart=True)
    column_menu = Regionplus(helper, column_menu.right())
    if not column_menu.Click(Pattern("1436391324903.png").similar(0.90),
        "Couldn't find arrow for drop-down menu, trying to expand column", give_up=False):
        
        # Click on hopefully a different test, so the view of our text will reset
        helper.Click(Pattern("Show.png").targetOffset(0, 30),
            "Couldn't find 'Show All'", time=3, restart=True)
        
        # Drag out the column so the arrow is visible
        while not column_menu.exists(Pattern("1436391324903.png").similar(0.90)):
            drag_point = helper.Find(Pattern("1436455824256.png").targetOffset(8,0), "Couldn't find point to drag out column", time=2, restart=True)
            drop_point = helper.Find(Pattern("Title.png").similar(0.90), "Couldn't find 'Title'", restart=True)
            dragDrop(drag_point, drop_point)
            
        # Click the arrow
        column_menu.Click(Pattern("1436391324903.png").similar(0.90),
            "Couldn't find arrow for drop-down menu even after expanding column", restart=True)
        
    helper.Click("lterfor.png", "'Filter for' button not found", restart=True)
    paste(text) 

    # Now the 'Filter for' box is up, so if we can't click something
    # we should restart Flex
    helper.Click(Pattern("W_holeitem.png").targetOffset(-42,0), "'Whole item' option not found", restart=True)
    helper.Click(Pattern("OK-1.png").similar(0.85), "OK button not found", time=10, restart=True)
    # 'Filter for' box is gone now, text should be selected automatically

    # Create a region inside the 'Text' panel
    text_header = helper.Find(Pattern("1439476758260.png").similar(0.90),
        "'Text' field not found in right panel", restart=True)
    below_region = text_header.below()
    right_region = text_header.right()
    text_region = Regionplus(helper, below_region.getX(),
                             below_region.getY(),
                             below_region.getW() + right_region.getW(),
                             below_region.getH())
    text_region.Click("PrintView.png", " Couldn't find 'Print View' tab", restart=True)

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
    
    helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button", restart=True)
    # First make sure all entries are showing
    LEFT_SIDEBAR.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button", time=10, restart=True)
    if not exists(Pattern("ieadwordShow.png").similar(0.90)):
        helper.Click(Pattern("LexemeForm.png").targetOffset(-52,23), "'Lexeme Form' column not found", restart=True)
        helper.Click(Pattern("Headword-1.png").similar(0.90).targetOffset(0,50), "Couldn't find 'Headword'", time=15, restart=True)
    
    LEFT_SIDEBAR.Click("ElDictionary.png", "Couldn't find 'Dictionary' button", time=20, restart=True)

    # Goal
    #################
    TOOLBARS.Click("1436456695019.png", "Couldn't find 'First' button -- may already be at start", give_up=False)
    if exists(Pattern(compare_path).similar(0.9)):
        helper.write("Dictionary looks the same as in provided image")
    else:
        helper.write("Dictionary print view has changed")
