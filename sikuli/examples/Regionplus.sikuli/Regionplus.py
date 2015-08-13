from sikuli import *

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
# Regionplus copies default arguments to wrapper functions
# from its TestHelper when the TestHelper is set. Note that
# these defaults can be overwritten afterwards, and different
# arguments can always be given at each method call.
#

class Regionplus(Region):

    def __init__(self, test_helper, *args):
        Region.__init__(self, *args)
        self.helper = test_helper

        if self.helper:
            self.time_default = self.helper.time_default
            self.giveup_default = self.helper.giveup_default
            self.restart_default = self.helper.restart_default
            self.successmsg_default = self.helper.successmsg_default
        else:
            self.time_default = 1
            self.giveup_default = True
            self.restart_default = False
            self.successmsg_default = None

    def set_helper(self, test_helper):
        self.helper = test_helper
        if self.helper:
            self.time_default = self.helper.time_default
            self.giveup_default = self.helper.giveup_default
            self.restart_default = self.helper.restart_default
            self.successmsg_default = self.helper.successmsg_default
        

    def Click(self, thing, fail_message, give_up=self.giveup_default,
              restart=self.restart_default,
              success_message=self.successmsg_default, time=self.time_default):
        try:
            self.click(thing)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Click", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def DoubleClick(self, thing, fail_message, give_up=self.giveup_default,
                    restart=self.restart_default,
                    success_message=self.successmsg_default, time=self.time_default):
        try:
            self.doubleClick(thing)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Double Click", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def Find(self, thing, fail_message, give_up=self.giveup_default,
             restart=self.restart_default,
             success_message=self.successmsg_default, time=self.time_default):
        try:
            match = self.find(thing)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return match
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Find", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Wait(self, thing, wait_time, fail_message, give_up=self.giveup_default,
             restart=self.restart_default,
             success_message=self.successmsg_default, time=self.time_default):

        try:
            match = self.wait(thing, wait_time)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return match
        except FindFailed:
            if self.helper:
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Appearance", thing)
            if restart:
                self.helper.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Exists(self, thing, fail_message, give_up=self.giveup_default,
               restart=self.restart_default,
               success_message=self.successmsg_default, time=self.time_default):
        if self.exists(thing):
            if success_message:
                self.helper.write(success_message)
            return True
        else:
            if self.helper:
                self.helper.write_fail(fail_message)
                self.helper.write_html_row("Existence", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
    
    def offset(self, x, y):
        return offset(Location(x, y))