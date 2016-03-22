from test_helper import *
import open_flex_from_backup

# Opening
#############

backups_folder = home_folder + "/Integration-Testing-Framework/flex/projects/"

# Open Tagbanwa
open_flex_from_backup.open_backup(backups_folder + "Tagbanwa, Calamian 2015-07-07 1037 for testing purposes.fwbackup", True)
wait(60)


# Filter for "agbas"
wait("LexiconEdit.png",300)
click("LexiconEdit.png")
wait(10)
click(Pattern("LexemeForm.png").targetOffset(-52,23))
click("lterfor.png")
paste("agbas")
type(Key.ENTER)
wait(15)

# Open Configure menu
click("Tools.png")
click("Configure.png")
click(Pattern("Dictionary-1.png").similar(0.95))

# Switch to Stem-based
if not exists("1439408395678.png"):
    click(Pattern("1439408329695.png").targetOffset(-54,0))
    click("Stembased.png")

# Uncheck all check boxes
main_entry = find("MainEntrv.png")
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
variant_forms = find("1439412239108.png")
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

click(Pattern("OK.png").similar(0.95))

# Go to Dictionary view and wait (up to 30 seconds) for it to load
click(Pattern("Dictionary.png").similar(0.90))
wait("MainDictiona.png", 30)

# Goal
###############
exists("frvarFreeVar.png")

App.focus("Tagbanwa")
click("1436902218392.png")