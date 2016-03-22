from test_helper import *
import check_change, open_flex_from_backup

folder = home_folder + "/Integration-Testing-Framework/sikuli/helpers/images_for_comparison/"
backups_folder = home_folder + "/Integration-Testing-Framework/flex/projects/"

# Open Tagbanwa
open_flex_from_backup.open_backup(backups_folder + "Tagbanwa, Calamian 2015-07-07 1037 for testing purposes.fwbackup", True)
wait(30)
check_change.check_dictionary(folder + "Tagbanwa - dictionary.png")
check_change.check_word("dalik", folder + "Tagbanwa - dalik.png") # IXTERMINATE
check_change.check_word("bugnawan", folder + "Tagbanwa - bugnawan.png")
App.focus("Tagbanwa")
click("1436902218392.png")

# Open Kamasau
open_flex_from_backup.open_backup(backups_folder + "Kamasau 2015-07-07 1036 for testing purposes.fwbackup", True)
wait(30)
check_change.check_dictionary(folder + "Kamasau - dictionary.png")
check_change.check_word("chiraq", folder + "Kamasau - chiraq.png") # like the French president in like the 2000s
check_change.check_word("gre", folder + "Kamasau - gre.png")
App.focus("Kamasau")
click("1436902218392.png")


# Open Ayta Mag-Anchi
open_flex_from_backup.open_backup(backups_folder + "Ayta Mag-Anchi2 2015-07-07 1035 for testing purposes.fwbackup", True)
wait(30)
check_change.check_text("kulot2.ptx", folder + "Ayta - kulot2.ptx.png")
App.focus("Ayta")
click("1436902218392.png")