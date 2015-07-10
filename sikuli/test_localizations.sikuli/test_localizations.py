from sikuli import *
import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')
from test_helper import TestHelper
from flex_regions import *

helper = TestHelper("test_localizations")
set_flex_helper(helper)
languages = ["Indonesian", "Malay", "English", "Spanish", "French",
    "Hungarian", "Portuguese", "Kinyarwanda", "Vietnamese", "Turkish",
    "Russian", "Farsi", "Hindi", "Telugu", "Korean", "Chinese"]

# Data for each area of the screen
areas = ["top toolbar (file, edit, etc.)", "blue headers",
    "left sidebar", "bottom left", "column headers",
    "'Show All' in column menus", "'Entry' panel", "bottom"]
area_regions = [Region(2,48,1148,36), Region(1,91,871,41), Region(0,122,144,231), Region(1,612,151,176),
    Region(139,117,405,35), Region(140,136,110,47), Region(645,88,516,702), Region(102,751,242,59)]
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
                 ["Lexicon", "Texts & Words", "Grammar", "Notebook", "Lists"],
                 ["Headword", "Lexeme Form", "Glosses", "Grammatical"],
                 ["Show All"],
                 ["Lexeme Form", "Morph Type", "Citation Form", "Components",
                   "Note", "Messages", "Gloss", "Definition", "Info.",
                   "Example", "Semantic Domains", "Lexical Relations",
                   "Category Info.", "Sense 1", "Variants", "Allomorphs",
                   "Grammatical Info. Details", "Publication"],
                 ["Queue", "No Parser Loaded"]]


for language in languages:

    # Opening: change UI to next language
    ################

    # Open Options popup
    wait(2)
    type("1", KeyModifier.ALT)
    for i in range(7):
        type(Key.RIGHT)
    for i in range(5):
        type(Key.DOWN)
    helper.Type(Key.ENTER)

    # Get to language drop-down menu
    type(Key.TAB)
    type(Key.TAB)
    
    # On first iteration, go to top of list, otherwise, go to next language.
    if language == "Indonesian":
        for i in range(len(languages)):
            type(Key.UP)
    else:
        type(Key.DOWN)

    type(Key.ENTER)
    wait(10)

    # GOAL
    ################

    for k in range(2, 3):
        area = areas[k]

        # First see if there is any English (note: cognates may be
        # flagged as not translated)
        if language != "English":
            # Check if whole area matches
            if area_regions[k].exists(Pattern(english_reference_images[k]).
                    similar(0.99)):
                helper.write(language + ": nothing translated in " + area)
                # If everything's in English, no need for more tests
                continue
            
            # Look for any English words
            words = english_words[k]
            for word in words:
                if area_regions[k].exists(word):
                    helper.write(language + ": '" + word + "' not translated in " + area)
        
            # Look for any placeholder squares
            if area_regions[k].exists(square_types[k]):
                helper.write(language + ": unable to render (placeholder boxes found) in " + area)


# Closing: Go back to English UI
##############

# Open Options popup
type("1", KeyModifier.ALT)
for i in range(7):
    type(Key.RIGHT)
for i in range(5):
    type(Key.DOWN)
helper.Type(Key.ENTER)

# Get to language drop-down menu
type(Key.TAB)
type(Key.TAB)
    
# Get to the top of the list, then go down to English
for i in range(len(languages)):
    type(Key.UP)
for i in range(languages.index("English")):
    type(Key.DOWN)
type(Key.ENTER)
wait(40)

helper.write("Finished testing UI localizations")