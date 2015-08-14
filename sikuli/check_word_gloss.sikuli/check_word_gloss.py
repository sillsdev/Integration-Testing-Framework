import a_setup
from test_helper import TestHelper
from Regionplus import Regionplus

helper = TestHelper("check_word_gloss")

# Make sure the word exists
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
helper.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button")
helper.Exists("asdfghasdfgh.png", "'asdfgh' word does not exist")

# Enter text if it's not there
helper.Click("VTexts6W0rc.png", "'Texts & Words' not found")
helper.Click(Pattern("Basehne.png").similar(0.90), "'Baseline' tab not found")
helper.Click("1438706667507.png", "Blank space not found")    # Move cursor to blank space
if not exists("1439580090308.png"):
    paste("asdfgh jjjj")

# View Gloss tab, make sure gloss is suggested and focus shifts
helper.Click(Pattern("Gloss-1.png").similar(0.81), "'Gloss' tab not found")
hover("1438706667507.png")    # Move to blank space so the hovertext doesn't appear
wait(2)
helper.Exists("asdfghhahaha.png", "'hahaha' gloss not suggested for 'asdfgh'")
helper.Click(Pattern("Luhukooo.png").targetOffset(-16,0), "Drop down menu not found")
helper.Click("Noun.png", "'Noun' not found")
type(Key.ENTER)
helper.Exists(Pattern("Luhukooo-1.png").similar(0.86), "'jjjj' word not in focus in Gloss tab")

# View Analyze tab, make sure focus is kept
helper.Click(Pattern("Analyze.png").similar(0.90), "'Analyze' tab not found")
hover("1438706667507-1.png")    # Move to blank space so the hovertext doesn't appear
helper.Exists(Pattern("LJLoooLJLooo.png").similar(0.80), "'jjjj' word not in focus in Analyze tab")

# Go back to Lexicon Edit
helper.Click("Lexicon.png", "Couldn't find 'Lexicon' button")
helper.Click("LexiconEdit.png", "Couldn't find 'Lexicon Edit' button")

helper.write_success()