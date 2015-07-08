from sikuli import *
import sys
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')
from test_helper import TestHelper
import open_flex_from_backup, check_change

helper = TestHelper("run_tests_from_backups")
folder = "/home/vagrant/linux_setup/sikuli/examples/images_for_comparison/"

# Open Tagbanwa
open_flex_from_backup.open_backup("/vagrant/flex projects/Tagbanwa, Calamian 2015-07-07 1037 for testing purposes.fwbackup", True)
# TODO: see if dictionary view has changed
check_change.check_word("dalik", folder + "Tagbanwa - dalik.png") # IXTERMINATE
check_change.check_word("bugnawan", folder + "Tagbanwa - bugnawan.png")

# Open Kamasau
open_flex_from_backup.open_backup("/vagrant/flex projects/Kamasau 2015-07-07 1036 for testing purposes.fwbackup", True)
# TODO: see if dictionary view has changed
check_change.word("chiraq", folder + "Kamasau - chiraq.png") # like the French president in like the 2000s
check_change.check_word("gre", folder + "Kamasau - gre.png")

# Open Ayta Mag-Anchi
open_flex_from_backup.open_backup("/vagrant/flex projects/Ayta Mag-Anchi2 2015-07-07 1035 for testing purposes.fwbackup", True)
check_change.check_text("kulot2.ptx", folder + "Ayta - kulot2.ptx.png")

helper.restart_flex()








