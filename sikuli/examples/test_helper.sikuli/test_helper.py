from __future__ import with_statement
from sikuli import *
import sys
import time
sys.path.insert(0, '/home/vagrant/linux_setup/sikuli/examples')

class TestHelper:

    # If a file with the given filename already exists, the Logger will
    # just keep writing to the end of that file.
    def __init__(self, test_name="", filename="/vagrant/error_log"):
        self.file = filename
        self.test = test_name + ": "
        self.test_failed = False

    #################################
    # Wrappers for click, type, etc
    #################################

    # Return True on success, False on FindFailed error, after
    # logging the error.
    # If give_up is True, exits the script using exit() on failure.
    # If restart is True, FLEX needs to be restarted on failure.

    def Click(self, thing, fail_message, give_up=True, restart=False,
              success_message=None, time=1):
        try:
            click(thing)
            if success_message:
                self.write(success_message)
            wait(time)
            return True
        except FindFailed:
            self.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def DoubleClick(self, thing, fail_message, give_up=True,
                    restart=False, success_message=None, time=1):
        try:
            doubleClick(thing)
            if success_message:
                self.write(success_message)
            wait(time)
            return True
        except FindFailed:
            self.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def Type(self, text, modifiers=0, time=1):
        type(text, modifiers)
        wait(time)
    
    def Find(self, thing, fail_message, give_up=True, restart=False,
             success_message=None, time=1):
        try:
            match = find(thing)
            if success_message:
                self.write(success_message)
            wait(time)
            return match
        except FindFailed:
            self.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Exists(self, thing, fail_message, give_up=True, restart=False,
               success_message=None, time=1):
        if exists(thing):
            if success_message:
                self.write(success_message)
            return True
        else:
            self.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False

    def restart_flex(self):
        self.write_fail("Closing and restarting FLEX")
        #os.system("sudo /home/vagrant/linux_setup/flex/flex_restart.sh")
        import restart_flex
        restart_flex.restart_flex()

    ###################
    # Logging methods
    ###################

    # Prepends the test name and appends a newline before writing to file.
    def write(self, line):
        with open(self.file, "a") as f:
            f.write(time.strftime("%I:%M:%S %x") + " " + self.test + line + "\n")

    # Same as write, but internally remembers that the test failed.
    def write_fail(self, line):
        self.test_failed = True
        self.write(line)

    # Returns whether any fails have been logged.
    def has_fail(self):
        return self.test_failed
    
    # Writes "Success" iff no fails have been recorded.
    def write_success(self):
        if not self.test_failed:
            self.write("Success")
