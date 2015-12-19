import xmlrunner
import sys
import unittest
import subprocess
import os

class FlexTests(unittest.TestCase):

    command = "sikuli-ide"
    line = "\n"
    boilerplate = 2

    #This does not work in Python 2.5 -- hence the static variables above.
    @classmethod
    def setUpClass(self):
        print "setting up class"
        self.myOS = Env.getOS()
        if self.myOS == OS.LINUX:
            self.command = "runsikulix"
            self.line = "\n"
            self.boilerplate = 2
        elif self.myOS == OS.WINDOWS:
            self.command = "runsikulix.cmd"
            self.line = "\r\n"
            self.boilerplate = 3
        else:
            print "Unsupported OS."

    def setUp(self):
        print ("\n"+time.strftime("%H:%M:%S %x") + " Running " + str.split(self.id(),".")[2][5:] + "... \n")

    def tearDown(self):
        pass

    def test_1_open_flex(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_check_keyboard_switching(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_check_suffix_formation(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_check_word_gloss(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_compare_screenshots_from_backups(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_create_lexicon_entry(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_create_new_text(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_create_notebook_entry(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_dictionary_variant_forms(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_drag_column(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_help_about(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_try_all_sidebar_buttons(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def test_zutalafin(self):
        output = self.run_sikuli_test(self.id())
        self.assertTrue('Success' in output)

    def run_sikuli_test(self,name):
        my_test = str.split(name,".")[2][5:] # test name of the form '__main__.MyTests.test_name', split on periods, then remove the 'test_'
        file = os.path.join(os.path.dirname(sys.argv[0]),"sikuli", my_test+".sikuli") # test location
        subprocess.call([self.command, '-r', file])
        for line in open("/vagrant/error_log"):
            last = line
        return last

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlexTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    xmlrunner.XMLTestRunner(file("/vagrant/unittest.xml", "w")).run(suite)
