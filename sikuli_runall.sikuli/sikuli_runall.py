import xmlrunner
import sys
import unittest
import subprocess
import os
import inspect
from sikuli import *
from test_helper import *

class FlexTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        if __name__ == '__main__':
            self.myFolder = getParentFolder()
        else:
            if myOS == sikuli.OS.LINUX:
                self.myFolder = os.path.dirname(__file__)
            elif myOS == sikuli.OS.WINDOWS:
                self.myFolder = os.path.dirname(os.path.dirname(__file__))
            elif myOS == OS.MAC:
                self.myFolder = os.path.dirname(__file__)

    def setUp(self):
        print ("\n"+time.strftime("%H:%M:%S %x") + " Running " + str.split(self.id(),".")[-1][5:] + "... \n")


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
        the_test = str.split(name,".")[-1][5:] # test name of the form '__main__.MyTests.test_name', split on periods, then remove the 'test_'
        file = os.path.join(self.myFolder, the_test+".sikuli") # test location
        #subprocess.call([self.command, '-r', file])
        runScript(file)
        for line in open("./error_log"):
            last = line
        return line

def load_tests(*args, **kwargs):
    print "Passed: ", args, kwargs
    suite = unittest.TestSuite()
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and issubclass(obj,unittest.TestCase):
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(obj))
    return suite

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlexTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    xmlrunner.XMLTestRunner(file("/vagrant/unittest.xml", "w")).run(suite)
