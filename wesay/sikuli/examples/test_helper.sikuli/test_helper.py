from __future__ import with_statement
import glob
import os
import platform
import shutil
import sys
import time


from sikuli import *

sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples')
sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples/test_and_log')
from yattag import Doc

class TestHelper:

    # If a file with the given filename already exists, the Logger will
    # just keep writing to the end of that file.
    def __init__(self, test_name="", filename="/vagrant/error_log",
                 log_folder="/vagrant/log"):
        self.file = filename
        self.folder = log_folder
        self.test = test_name
        self.test_failed = False

        # Determine which OS we're on
        self.os = Env.getOS()

        # Create the log folder if it doesn't exist
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
            self.partial_html = self.folder + "/mylog.log"
        # Otherwise, see if there's already a log file
        else:
            glob_result = glob.glob(self.folder + "/*.log")
            if len(glob_result) == 1:
                self.partial_html = glob_result
            else:
                self.partial_html = self.folder + "/mylog.log"
        
        # Add the CSS stylesheet to the log folder, if it's not there already.
        if not os.path.exists(log_folder + "/log.css"):
            shutil.copyfile("/home/vagrant/Integration-Testing-Framework/sikuli/examples/test_helper.sikuli/log.css",
                            log_folder + "/log.css")

        # Add the display_log script to /vagrant, if it's not there
        # (so it's accessible from the host machine)
        if not os.path.exists("/vagrant/display_log.py"):
            shutil.copyfile("/home/vagrant/Integration-Testing-Framework/sikuli/examples/test_helper.sikuli/display_log.py",
                            "/vagrant/display_log.py")

    #################################
    # Wrappers for click, type, etc
    #################################

    # Return True on success, False on FindFailed error, after
    # logging the error.
    # If give_up is True, exits the script using exit() on failure.
    # If restart is True, FLEx is restarted on failure.

    def Click(self, thing, fail_message, give_up=True, restart=False,
              success_message=None, time=2):
        try:
            click(thing)
            if success_message:
                self.write(success_message)
            wait(time)
            return True
        except FindFailed:
            self.write_fail(fail_message)
            self.write_html_row("Click", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise

    def DoubleClick(self, thing, fail_message, give_up=True,
                    restart=False, success_message=None, time=2):
        try:
            doubleClick(thing)
            if success_message:
                self.write(success_message)
            wait(time)
            return True
        except FindFailed:
            self.write_fail(fail_message)
            self.write_html_row("Double Click", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise

    def Type(self, text, modifiers=0, time=2):
        type(text, modifiers)
        wait(time)

    def Find(self, thing, fail_message, give_up=True, restart=False,
             success_message=None, time=2):
        try:
            match = find(thing)
            if success_message:
                self.write(success_message)
            wait(time)
            return match
        except FindFailed:
            self.write_fail(fail_message)
            self.write_html_row("Find", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Exists(self, thing, fail_message, give_up=True, restart=False,
               success_message=None):

        if exists(thing):
            if success_message:
                self.write(success_message)
            return True
        else:
            self.write_fail(fail_message)
            self.write_html_row("Existence", thing)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False

    def restart_flex(self):
        self.write_fail("Closing and restarting FLEx")
        # os.system("sudo -u vagrant /home/vagrant/Integration-Testing-Framework/flex/flex_restart.sh")
        import restart_flex
        restart_flex.restart_flex()

    def get_os(self):
        return self.os

    ###################
    # Logging methods
    ###################

    # Prepends the time and test name and appends a newline before writing to file.
    def write(self, line):
        with open(self.file, "a") as f:
            f.write(time.strftime("%I:%M:%S %x") + " " + self.test + ": " + line + "\n")

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

    # Copy a file into the log folder and return just the name of the file.
    def copy_testfile(self, file_to_copy):
        name = os.path.basename(file_to_copy)
        new_path = self.folder + "/" + name
        shutil.copyfile(file_to_copy, new_path)
        return name

    # Find an image file in sys.path. If not found, or
    # not a valid image, return an empty string.
    def find_valid_image(self, img):
        valid_extensions = ["png", "jpg", "jpeg"]
        split_result = img.split('.')
    
        # If no '.': not a file
        if len(split_result) <= 1:
            return ""
        # If there is only one '.' and nothing before it, not a file
        elif len(split_result) == 2 and  split_result[0] == "":
            return ""
        # If it doesn't end in a valid extension, not an image file
        elif split_result[-1] not in valid_extensions:
            return ""
        # If it's an absolute path (that passed the file extension
        # tests), return it
        elif os.path.isfile(img):
            return img
        
        # Look in all the sys.path dirs to see if it's there
        for dir in sys.path:
            if dir[-1] != '/':
                dir = dir + '/'
            # If found, return the full path
            if os.path.isfile(dir + img):
                return dir + img
    
        return ""

    # Write a log entry into the "mylog.log" file in the log
    # folder, in the form of an html table row (<tr>).
    def write_html_row(self, action_type, expected):
        doc, tag, text = Doc().tagtext()

        # Create the row
        # Test name, Action, Expected, Screenshot
        with tag("tr"):
            with tag("td"):
                text(time.strftime("%I:%M:%S %x"))
            with tag("td"):
                text(self.test)
            with tag("td"):
                text(action_type)
            with tag("td"):
                # If 'expected' is given, figure out what kind
                # of thing it is
                if expected:
                    if isinstance(expected, str):
                        full_path = self.find_valid_image(expected)

                        # If a path was found, add a clickable image.
                        # If not, add text.
                        if full_path:
                            expected_path = self.copy_testfile(full_path)
                            with tag("a", href=expected_path):
                                doc.stag("img", src=expected_path)
                        else:
                            text(expected)
                    # If it's a pattern, get the image
                    elif isinstance(expected, Pattern):
                        full_path = self.find_valid_image(expected.getFilename())
                        expected_path = self.copy_testfile(full_path)
                        with tag("a", href=expected_path):
                            doc.stag("img", src=expected_path)
                    # If it's a match or a region, take a
                    # screenshot of the area
                    elif (isinstance(expected, Match) or
                          isinstance(expected, Region)):
                        screencap = capture(expected)
                        expected_path = self.copy_testfile(screencap)
                        with tag("a", href=expected_path):
                            doc.stag("img", src=expected_path)
                    elif isinstance(expected, Location):
                        # Create an area 50px around the location
                        r = Region(expected.getX(), expected.getY(), 0, 0)
                        r = r.nearby()
                        # take a screenshot
                        screencap = capture(r)
                        expected_path = self.copy_testfile(screencap)
                        with tag("a", href=expected_path):
                            doc.stag("img", src=expected_path)

            with tag("td"):
                # Take screenshot
                screenshot = capture(SCREEN)
                screenshot_path = self.copy_testfile(screenshot)
                with tag("a", href=screenshot_path):
                    doc.stag("img", src=screenshot_path)

        # Write the row to the partial html file
        with open(self.partial_html, "a") as f:
            f.write(doc.getvalue())
