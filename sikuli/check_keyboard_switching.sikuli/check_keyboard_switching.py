import a_setup
a_setup.giveup_default=False
from test_helper import TestHelper
from Regionplus import Regionplus
a_setup.giveup_default=True

# Note: if anything fails after the keyboard is set to French,
# try to switch it back to English before shutting down.

helper = TestHelper("check_keyboard_switching")
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
helper.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button", give_up=True)

# If always_restart is on, restart when clicks fail even if
# the dialog box is not supposed to be open.
# (used when trying to set the keyboard back to English, when
# trying to recover from another error.)
def open_keyboard_selection(always_restart):
    helper.Click(Pattern("Format.png").similar(0.80), "'Format' not found", give_up=True, restart=always_restart)
    helper.Click("SetupWriting.png", "'Set up Writing Systems' not found in Format menu", give_up=True, restart=always_restart)
    analysis = helper.Find("Analysis_Wri-1.png", "'Analysis Writing Systems' not found", restart=True)
    Regionplus(helper, analysis.above().right()).Click("Modify.png",
        "'Modify...' button not found above and to the right of 'Analysis Writing Systems'",
        restart=True)
    helper.Click(Pattern("f__AIII_l__l.png").similar(0.80), "'Keyboard' tab not found", restart=True)

def close_keyboard_selection():
    for i in range(2): 
        helper.Click(Pattern("OK.png").similar(0.90), "OK button not found", restart=True)

def set_english_keyboard():
    open_keyboard_selection(True)
    helper.Click("EnqlishUSEnq.png", "English keyboard not found", restart=True)
    close_keyboard_selection()

def recover():
    app_region = helper.Find("1438702584115.png", "'Applications' not found", restart=True)
    exclude_height = 2 * app_region.getH()
    screen_region = Region(0, exclude_height, SCREEN.getW(),
                           SCREEN.getH() - exclude_height)
    
    while screen_region.exists(Pattern("X.png").similar(0.90)):
        helper.Click(Pattern("X.png").similar(0.90), "Tried to close window", restart=True)
    set_english_keyboard()
    exit()


# Set Vernacular keyboard to French
open_keyboard_selection(False)
helper.Click("FrenchFrench.png", "French keyboard not found", restart=True)
close_keyboard_selection()

# Create new entry
if not helper.Click("1435675185765.png", "'Create new lexical entry' button not found"):
    recover()
paste("asdfgh")
if not helper.Click(Pattern("Gloss.png").similar(0.90).targetOffset(-10,21), "'Gloss' field not found"):
    recover()
paste("hahaha")
if not helper.Click(Pattern("Create.png").similar(0.90), "'Create' button not found", time=3):
    recover()

# Verify input languages
if not helper.Click(Pattern("FreLexemeFON.png").targetOffset(114,4), "'Lexeme Form' field not found"):
    recover()
Regionplus(helper, find("1438702584115.png").right()).Exists("Eh-1.png",
    "Lexeme Form field input keyboard not in French")
if not helper.Click(Pattern("EngNote.png").targetOffset(94,1), "'Note' field not found"):
    recover()
Regionplus(helper, find("1438702584115.png").right()).Exists("Een-1.png",
    "Note field input keyboard not in English")

helper.write_success()

# Change keyboard back to English to avoid side effects
set_english_keyboard()