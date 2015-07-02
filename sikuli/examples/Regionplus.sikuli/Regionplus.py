from sikuli import *

class Regionplus(Region):

    def __init__(self, test_helper, *args):
        Region.__init__(self, *args)
        self.helper = test_helper

    def set_helper(self, test_helper):
        self.helper = test_helper
        

    def Click(self, thing, fail_message, give_up=True, restart=False,
              success_message=None, time=1):
        try:
            self.click(thing)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def DoubleClick(self, thing, fail_message, give_up=True, restart=False,
                    success_message=None, time=1):
        try:
            self.doubleClick(thing)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise
    
    def Find(self, thing, fail_message, give_up=True, restart=False,
             success_message=None, time=1):
        try:
            match = self.find(thing)
            if success_message:
                self.helper.write(success_message)
            wait(time)
            return match
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Exists(self, thing, fail_message, give_up=True, restart=False,
               success_message=None, time=1):
        if self.exists(thing):
            if success_message:
                self.helper.write(success_message)
            return True
        else:
            if self.helper:
                self.helper.write_fail(fail_message)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
    
    def offset(self, x, y):
        return offset(Location(x, y))