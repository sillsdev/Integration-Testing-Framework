from a_setup import *
from test_helper import TestHelper
from Regionplus import Regionplus

helper = TestHelper("check_suffix_formation")

# Make sure the word exists
wait("Lexicon.png",300)
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
helper.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button")
helper.Exists("asdfghasdfgh.png", "'asdfgh' word does not exist")

# Enter text if it's not there
helper.Click("VTexts6W0rc.png", "'Texts & Words' not found")
helper.Click(Pattern("Basehne.png").similar(0.90), "'Baseline' tab not found")
helper.Click("1438706667507.png", "Blank space not found")    # Move cursor to blank space
if not exists("1439580090308.png"):
    paste("asdfgh jjjj")

# View Analyze tab, put jjjj in focus
helper.Click(Pattern("Analyze.png").similar(0.90), "'Analyze' tab not found")
hover("1438706667507-2.png")    # Move to blank space so the hovertext doesn't appear
if not exists(Pattern("LJLoooLJLooo.png").similar(0.80)):
    helper.Click("LukuboouLuku.png", "jjjj word not found")    

# Split word
helper.Click(Pattern("1438704084589.png").targetOffset(4,2), "'jjjj' not found on Morpheme line")
type("-")
helper.Exists(Pattern("1438704193830.png").similar(0.90), "Word not split into two morphemes")

# Verify that second morpheme is a suffix
helper.Click(Pattern("LJLoooLJLooo-1.png").targetOffset(10,0), "Drop down menu not found")
helper.Click("CreateNewEnt.png", "'Create New Entry' not found in drop down menu")
wait(2)
helper.Exists(Pattern("MorphemeType.png").similar(0.90), "Morpheme type not listed as '-suffix'")
helper.Click(Pattern("Cancel.png").similar(0.91), "'Cancel' button not found", restart=True)

# Put 'jjjj' back into one word so the test works next time
# Maybe not necessary? Since a new project gets created every time
# all scripts are run....
helper.Click(Pattern("1438704193830-1.png").targetOffset(-37,1), "Drop down menu not found")
helper.Click(Pattern("1438706343069.png").similar(0.95).targetOffset(-23,1), "'jjjj' option not found in drop down menu")
helper.Click("Lexicon-1.png", "'Lexicon' button not found")


helper.write_success()