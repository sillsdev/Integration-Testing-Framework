from sikuli import *
from test_helper import *

def check_word(word, compare_path):

    # Opening
    ###############
    wait("Lexicon.png",60)
    click("Lexicon.png")
    LEFT_SIDEBAR.click("LexiconEdit.png")
    wait(10)
    click(Pattern("LexemeForm.png").targetOffset(-52,23))
    click("lterfor.png")
    paste(word)
    
    # Now the 'Filter for' box is up, so if we can't click something
    # we should restart Flex
    click(Pattern("W_holeitem.png").targetOffset(-42,0))
    click(Pattern("OK-1.png").similar(0.85))
    wait(10)
    # 'Filter for' box is gone now, word should be selected automatically
    
    
    # Create a region inside the 'Entry' panel
    entry_header = find("9Entry.png",
        "'Entry' field not found in right panel") 
    below_region = entry_header.below()
    right_region = entry_header.right()
    entry_region = Region(below_region.getX(), below_region.getY(),
                          below_region.getW() + right_region.getW(),
                          below_region.getH())
    
    # Goal
    ###############
    if entry_region.exists(Pattern(compare_path).similar(0.9)):
        Debug.user("'" + word + "' field looks the same as in provided image")
    else:
        Debug.user("'" + word + "' field has changed")


def check_text(text, compare_path):
    # Opening
    ###############
    wait("TUTextsWord.png", 60) 
    click("TUTextsWord.png")
    LEFT_SIDEBAR.wait("InterlinearT.png",60)
    LEFT_SIDEBAR.click("InterlinearT.png")
    
    # Find the menu to search for text
    column_menu = find("Show.png")
    column_menu = column_menu.right()
    if not column_menu.click(Pattern("1436391324903.png").similar(0.90)):
        
        # Click on hopefully a different test, so the view of our text will reset
        click(Pattern("Show.png").targetOffset(0, 30))
        wait(3)
        
        # Drag out the column so the arrow is visible
        while not column_menu.exists(Pattern("1436391324903.png").similar(0.90)):
            drag_point = find(Pattern("1436455824256.png").targetOffset(8,0))
            wait(2)
            drop_point = find(Pattern("Title.png").similar(0.90))
            dragDrop(drag_point, drop_point)
            
        # Click the arrow
        column_menu.click(Pattern("1436391324903.png").similar(0.90))
        
    click("lterfor.png")
    paste(text) 

    # Now the 'Filter for' box is up, so if we can't click something
    # we should restart Flex
    click(Pattern("W_holeitem.png").targetOffset(-42,0))
    click(Pattern("OK-1.png").similar(0.85))
    wait(10)
    # 'Filter for' box is gone now, text should be selected automatically

    # Create a region inside the 'Text' panel
    text_header = find(Pattern("1439476758260.png").similar(0.90))
    below_region = text_header.below()
    right_region = text_header.right()
    text_region = Region(below_region.getX(),
                             below_region.getY(),
                             below_region.getW() + right_region.getW(),
                             below_region.getH())
    text_region.click("PrintView.png")

    # Goal
    ###############
    if text_region.exists(Pattern(compare_path).similar(0.9)):
        Debug.user("'" + text + "' print view looks the same as in provided image")
    else:
        Debug.user("'" + text + "' print view has changed")


def check_dictionary(compare_path):

    # Opening
    ################
    wait("Lexicon.png", 60)
    click("Lexicon.png")
    # First make sure all entries are showing
    LEFT_SIDEBAR.click("LexiconEdit.png")
    wait(10)
    if not exists(Pattern("ieadwordShow.png").similar(0.90)):
        click(Pattern("LexemeForm.png").targetOffset(-52,23))
        click(Pattern("Headword-1.png").similar(0.90).targetOffset(0,50))
        wait(15)
    
    LEFT_SIDEBAR.click("ElDictionary.png")
    wait(20)

    # Goal
    #################
    TOOLBARS.click("1436456695019.png")
    if exists(Pattern(compare_path).similar(0.9)):
        Debug.user("Dictionary looks the same as in provided image")
    else:
        Debug.user("Dictionary print view has changed")
