from sikuli import *
from a_setup import *

#
# This class provides the same wrapper methods as TestHelper,
# but when acting on regions rather than the whole screen.
# A TestHelper instance must be set for the logging to occur,
# either on initialization or with the set_helper method.
# A Regionplus object can be created from any Region object
# or by any other Region constructor; the first
# argument to the Regionplus constructor must be the TestHelper
# (use a None placeholder if not providing a TestHelper.)
#
# time_default, giveup_default, restart_default, successmsg_default
# all configure default behavior for the wrapper methods.
# They are set in a_setup, and can be modified there.
#

class Regionplus(Region):

    def __init__(self, test_helper, *args):
        Region.__init__(self, *args)
        self.helper = test_helper

    def set_helper(self, test_helper):
        self.helper = test_helper

    # Wrapper methods:
    # Return True on success, False on FindFailed error;
    # in relevant cases, return instead a Match object on success,
    # None on error.
    # In case of success, wait the number of seconds specified by time.
    # Log errors in both text and html logs. If a success message
    # is given, log success in text log.
    # If give_up is True, exit the script using exit() on failure.
    # If restart is True, FLEx is restarted on failure.


    def Click(self, thing, fail_message, give_up=giveup_default,
              restart=restart_default,
              success_message=successmsg_default, time=time_default):
        try:
            screenshot = capture(SCREEN)
            self.click(thing)
            self.helper.write_html_row("Click", thing, "Success", screenshot)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                screenshot = capture(SCREEN)
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Click", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise

    def DoubleClick(self, thing, fail_message, give_up=giveup_default,
                    restart=restart_default,
                    success_message=successmsg_default, time=time_default):
        try:
            screenshot = capture(SCREEN)
            self.doubleClick(thing)
            self.helper.write_html_row("Double Click", thing, "Success", screenshot)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                screenshot = capture(SCREEN)
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Double Click", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def Find(self, thing, fail_message, give_up=giveup_default,
             restart=restart_default,
             success_message=successmsg_default, time=time_default):
        try:
            screenshot = capture(SCREEN)
            match = self.find(thing)
            self.helper.write_html_row("Find", thing, "Success", screenshot)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return match
        except FindFailed, ff:
            if self.helper:
                screenshot = capture(SCREEN)
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Find", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Wait(self, thing, wait_time, fail_message, give_up=giveup_default,
             restart=restart_default,
             success_message=successmsg_default, time=time_default):

        try:
            screenshot = capture(SCREEN)
            match = self.wait(thing, wait_time)
            self.helper.write_html_row("Appearance", thing, "Success", screenshot)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return match
        except FindFailed:
            if self.helper:
                screenshot = capture(SCREEN)
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Appearance", thing, "Fail", screenshot)
            if restart:
                self.helper.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Exists(self, thing, fail_message, give_up=giveup_default,
               restart=restart_default,
               success_message=successmsg_default):

        screenshot = capture(SCREEN)
        if self.exists(thing):
            self.helper.write_html_row("Existence", thing, "Success", screenshot)
            if success_message:
                self.helper.write(success_message)
            return True
        else:
            if self.helper:
                screenshot = capture(SCREEN)
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Existence", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
    
    def offset(self, x, y):
        return offset(Location(x, y))