from a_setup import *
from test_helper import TestHelper

helper = TestHelper("help_about")

# Opening
#############

# Filter for "agbas"
helper.Click("LexiconEdit-1.png", "'Lexicon Edit' not found", time=10)
helper.Click(Pattern("LexemeForm.png").targetOffset(-52,23), "'Lexeme Form' column not found")
helper.Click("lterfor.png", "'Filter for' button not found")
paste("agbas")
type(Key.ENTER)
wait(15)

# Open Configure menu
helper.Click("Tools.png", "'Tools' menu not found")
helper.Click("Configure.png", "'Configure' menu not found")
helper.Click(Pattern("Dictionary-1.png").similar(0.95), "'Dictionary...' menu not found")

# Switch to Stem-based
if not exists("1439408395678.png"):
    helper.Click(Pattern("1439408329695.png").targetOffset(-54,0), "Drop down menu next to 'Manage Views' not found")
    helper.Click("Stembased.png", "'Stem-based' not found")

# Uncheck all check boxes
main_entry = helper.Find("MainEntrv.png", "'Main Entry' not found")
click(main_entry)

# Get the region under and to the right of Main Entry
under = main_entry.below()
rightt = main_entry.right()
myregion = Region(under.getX(), under.getY(),
    under.getW() + rightt.getW(), under.getH())

while not myregion.exists("MinorEntrv.png"):
    while myregion.exists(Pattern("1439410798330.png").similar(0.85)):
        myregion.click(Pattern("1439410798330.png").similar(0.85))
    type(Key.PAGE_DOWN)
while myregion.exists(Pattern("1439410798330.png").similar(0.85)):
        myregion.click(Pattern("1439410798330.png").similar(0.85))

# Check the Variant Forms boxes
while not exists("VariantForms.png"):
    type(Key.PAGE_UP)
click("VariantForms.png")
variant_forms = helper.Find("1439412239108.png", "'Variant Forms' not found")
focus_region = variant_forms

# This assumes all the "Variant Forms" options (expanded), and
# "Etymology" (collapsed) are on the same screen, with no scrolling.
while not focus_region.exists("Etvmoloav.png"):
    # Check box if unchecked
    if not focus_region.exists(Pattern("1439410798330.png").similar(0.85)):
        type(Key.SPACE)
    # Move focus region down 16 px
    focus_region = focus_region.offset(Location(0, 16))
    type(Key.DOWN)

helper.Click(Pattern("OK.png").similar(0.95), "'OK' button not found")

# Go to Dictionary view and wait (up to 30 seconds) for it to load
helper.Click(Pattern("Dictionary.png").similar(0.90), "'Dictionary' not found")
helper.Wait("MainDictiona.png", 30, "Dictionary loading timed out")

# Goal
###############
helper.Exists("frvarFreeVar.png", "Variant Forms dictionary view incorrect")
helper.write_success()