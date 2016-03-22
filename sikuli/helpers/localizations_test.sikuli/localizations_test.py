from sikuli import *
from test_helper import *

languages = ["Indonesian", "Malay", "English", "Spanish", "French",
        "Hungarian", "Portuguese", "Kinyarwanda", "Vietnamese", "Turkish",
        "Russian", "Farsi", "Hindi", "Telugu", "Korean", "Chinese"]

# If this is True, the script will compare each string on the
# Lexicon Entry screen with the English strings. Otherwise,
# it will only compare whole areas of the screen, and look
# for font problems (i.e. those placeholder box things.)
see_if_things_are_translated = True

# Data for each area of the screen
areas = ["top toolbar (file, edit, etc.)", "blue headers",
    "left sidebar", "bottom left", "column headers",
    "'Show All' in column menus", "'Entry' panel", "bottom"]
area_regions = [Region(0,53,1024,21), Region(0,98,729,24), Region(0,124,141,153), Region(0,548,145,174),
    Region(145,124,435,19), Region(144,144,98,29), Region(584,98,440,625), Region(43,720,192,24)]
square_types = ["square_beige-1.png", "square_blue.png", "square_white_left.png", "square_beige_gradient.png", "square_beige_middle.png", "square_white_left.png", "square_white_right.png", "square_white_left.png"]
english_reference_images = ["file_edit_toolbar.png",
    "blue_headers_lexicon.png",
   "left_menu_lexicon.png", "lexicon_notebook_etc.png", "lexicon_edit_columns.png", "lexicon_edit_column_menus.png", "entry_panel_cat.png", "bottom_bar_lexicon_edit.png"]
english_words = [["File", "Send/Receive", "Edit", "View", "Data", "Insert", "Format",
                  "Tools", "Parser", "Window", "Help"],
                 ["Lexicon", "Entries", "Entry"],
                 ["Lexicon Edit", "Browse", "Dictionary", "Words",
                  "Classified Dictionary", "Bulk Edit Entries",
                  "Reversal Indexes", "Bulk Edit Reversal", "Edit"],
                 ["Lexicon", "Texts & W", "Grammar", "Notebook", "Lists"],
                 ["Headword", "Lexeme Form", "Glosses", "Grammatical"],
                 ["Show All"],
                 ["Lexeme Form", "Morph Type", "Citation Form", "Components",
                   "Note", "Messages", "Gloss", "Definition", "Info.",
                   "Example", "Semantic Domains", "Lexical Relations",
                   "Category Info.", "Sense 1", "Variants", "Allomorphs",
                   "Grammatical Info. Details", "Publication"],
                 ["Queue", "No Parser Loaded"]]

for r in area_regions:
    r.setAutoWaitTimeout(1)
    
def run_test(language_idx):

    setAutoWaitTimeout(1)
    
    # Opening: change UI to the language we want
    ################

    # Open Options popup
    wait(5)
    type("1", KeyModifier.ALT)
    for i in range(7):
        type(Key.RIGHT)
        wait(.5)
    for i in range(5):
        type(Key.DOWN)
        wait(.5)
    type(Key.ENTER)
    wait(.5)
    # Get to language drop-down menu
    type(Key.TAB)
    wait(.5)
    type(Key.TAB)
    wait(.5)
    # Get to the right language
    for i in range(len(languages)):
        type(Key.UP)
        wait(.5)
    for i in range(language_idx):
        type(Key.DOWN)
        wait(.5)

    type(Key.ENTER)
    wait(10)

    # GOAL
    ################

    if False: #Change to True if you want images captured
        import shutil
        shutil.copyfile(capture(SCREEN), "/vagrant/test_" + languages[language_idx].lower() + "_localization.png")
    else:
        for k in range(len(areas)):
            area = areas[k]

            # First see if there is any English (note: cognates may be
            # flagged as not translated)
            if language_idx != 2:
                # Check if whole area matches
                if area_regions[k].exists(Pattern(english_reference_images[k]).
                        similar(0.99)):
                    Debug.user("Nothing translated in " + area)
                    # If everything's in English, no need for more tests
                    continue

                # Look for any English words
                if see_if_things_are_translated:
                    words = english_words[k]
                    for word in words:
                        if area_regions[k].exists(word):
                            Debug.user("'" + word + "' not translated in " + area)
            
            # Look for any placeholder squares
            #if area_regions[k].exists(square_types[k]):
            #    Debug.user("---","FAIL","Unable to render (placeholder boxes found) in " + area)

    
    # Closing: Go back to English UI
    ##############
    
    # Open Options popup
    type("1", KeyModifier.ALT)
    for i in range(7):
        type(Key.RIGHT)
        wait(.5)
    for i in range(5):
        type(Key.DOWN)
        wait(.5)
    type(Key.ENTER)
    wait(.5)
    
    # Get to language drop-down menu
    type(Key.TAB)
    wait(.5)
    type(Key.TAB)
    wait(.5)
        
    # Get to the top of the list, then go down to English
    for i in range(len(languages)):
        type(Key.UP)
        wait(.5)
    for i in range(languages.index("English")):
        type(Key.DOWN)
        wait(.5)
    type(Key.ENTER)
    wait(40)
