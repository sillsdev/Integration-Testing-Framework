from sikuli import *
import a_setup
a_setup.restart_default = True
from test_helper import TestHelper
a_setup.restart_default = False
from a_setup import *
import check_change, open_flex_from_backup

helper = TestHelper("run_tests_from_backups")
folder = a_setup.home_folder + "/Integration-Testing-Framework/sikuli/examples/images_for_comparison/"
backups_folder = a_setup.home_folder + "/Integration-Testing-Framework/flex/projects/"

# Open Tagbanwa
open_flex_from_backup.open_backup(backups_folder + "Tagbanwa, Calamian 2015-07-07 1037 for testing purposes.fwbackup", True)
wait(60)
check_change.check_dictionary(folder + "Tagbanwa - dictionary.png")
check_change.check_word("dalik", folder + "Tagbanwa - dalik.png") # IXTERMINATE
check_change.check_word("bugnawan", folder + "Tagbanwa - bugnawan.png")
App.focus("Tagbanwa")
helper.Click("1436902218392.png", "Cannot find orange close button")

# Open Kamasau
open_flex_from_backup.open_backup(backups_folder + "Kamasau 2015-07-07 1036 for testing purposes.fwbackup", True)
wait(60)
check_change.check_dictionary(folder + "Kamasau - dictionary.png")
check_change.check_word("chiraq", folder + "Kamasau - chiraq.png") # like the French president in like the 2000s
check_change.check_word("gre", folder + "Kamasau - gre.png")
App.focus("Kamasau")
helper.Click("1436902218392.png", "Cannot find orange close button")


# Open Ayta Mag-Anchi
open_flex_from_backup.open_backup(backups_folder + "Ayta Mag-Anchi2 2015-07-07 1035 for testing purposes.fwbackup", True)
wait(60)
check_change.check_text("kulot2.ptx", folder + "Ayta - kulot2.ptx.png")
App.focus("Ayta")
helper.Click("1436902218392.png", "Cannot find orange close button")

# Restart flex to hello project, closing the 3 windows
# we just opened + whatever was open before
###helper.restart_flex()

helper.write_success()








