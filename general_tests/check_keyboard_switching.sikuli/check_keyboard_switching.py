from test_helper import *

# Note: if anything fails after the keyboard is set to French,
# try to switch it back to English before shutting down.

wait("Lexicon.png",300)
click("Lexicon.png")
click("LexiconEdit.png")

# If always_restart is on, restart when clicks fail even if
# the dialog box is not supposed to be open.
# (used when trying to set the keyboard back to English, when
# trying to recover from another error.)
def open_keyboard_selection():
    click(Pattern("Format.png").similar(0.80))
    click("SetupWriting.png")
    analysis = find("Analysis_Wri-1.png")
    analysis.above().right().click("Modify.png")
    click(Pattern("f__AIII_l__l.png").similar(0.80))

def close_keyboard_selection():
    for i in range(2): 
        click(Pattern("OK.png").similar(0.90))

def set_english_keyboard():
    open_keyboard_selection()
    click("EnqlishUSEnq.png")
    close_keyboard_selection()

def recover():
    app_region = find("1438702584115.png")
    exclude_height = 2 * app_region.getH()
    screen_region = Region(0, exclude_height, SCREEN.getW(),
                           SCREEN.getH() - exclude_height)
    
    while screen_region.exists(Pattern("X.png").similar(0.90)):
        click(Pattern("X.png").similar(0.90))
    set_english_keyboard()
    exit()


# Set Vernacular keyboard to French
open_keyboard_selection()
click("FrenchFrench.png")
close_keyboard_selection()

# Create new entry
if not click("1435675185765.png"):
    recover()
paste("asdfgh")
if click(Pattern("Gloss.png").similar(0.90).targetOffset(-10,21)):
    recover()
paste("hahaha")
if click(Pattern("Create.png").similar(0.90)):
    wait(3)
    recover()

# Verify input languages
if not click(Pattern("FreLexemeFON.png").targetOffset(114,4)):
    recover()
find("1438702584115.png").right().exists("Eh-1.png")
if not click(Pattern("EngNote.png").targetOffset(94,1)):
    recover()
find("1438702584115.png").right().exists("Een-1.png")

# Change keyboard back to English to avoid side effects
set_english_keyboard()