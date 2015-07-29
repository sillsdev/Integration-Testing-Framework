from sikuli import *
import a_setup
from test_helper import TestHelper
import open_flex_from_backup, check_change

helper = TestHelper("run_tests_from_backups")
folder = "/home/vagrant/Integration-Testing-Framework/sikuli/examples/images_for_comparison/"
backups_folder = "/home/vagrant/Integration-Testing-Framework/flex/projects/"

# Open Tagbanwa
open_flex_from_backup.open_backup(backups_folder + "Tagbanwa, Calamian 2015-07-07 1037 for testing purposes.fwbackup", True)
check_change.check_dictionary(folder + "Tagbanwa - dictionary.png")
check_change.check_word("dalik", folder + "Tagbanwa - dalik.png") # IXTERMINATE
check_change.check_word("bugnawan", folder + "Tagbanwa - bugnawan.png")

# Open Kamasau
open_flex_from_backup.open_backup(backups_folder + "Kamasau 2015-07-07 1036 for testing purposes.fwbackup", True)
check_change.check_dictionary(folder + "Kamasau - dictionary.png")
check_change.check_word("chiraq", folder + "Kamasau - chiraq.png") # like the French president in like the 2000s
check_change.check_word("gre", folder + "Kamasau - gre.png")

# Open Ayta Mag-Anchi
open_flex_from_backup.open_backup(backups_folder + "Ayta Mag-Anchi2 2015-07-07 1035 for testing purposes.fwbackup", True)
check_change.check_text("kulot2.ptx", folder + "Ayta - kulot2.ptx.png")

# Restart flex to hello project, closing the 3 windows
# we just opened + whatever was open before
helper.restart_flex()








