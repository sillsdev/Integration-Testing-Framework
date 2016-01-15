from __future__ import with_statement
from a_setup import *
from sikuli import *
import glob
import platform
import shutil
import time

#
# This class provides a logging system and wrappers for common
# Sikuli functions (click, doubleClick, type, find, wait, exists).
# One instance of a TestHelper should be created for each test.
#
# time_default, giveup_default, restart_default, successmsg_default
# all configure default behavior for the wrapper methods (see
# comment above the methods for a description of the individual
# variables.) They are set in a_setup, and can be modified there.
#
# The instance variable test_failed keeps track of whether or not a
# failure has been logged. It is set to True whenever one of the
# wrapper methods fails, but can also be set manually.
# 


if wd + "/helpers/test_and_log" not in sys.path:
    sys.path.append(wd + "/helpers/test_and_log")
from yattag import Doc

class TestHelper:

    # If a file with the given filename already exists, the Logger will
    # just keep writing to the end of that file.
    # filename is the path to the text log. If a file with the given
    # filename already exists, the Logger will just keep writing
    # to the end of that file.
    # log_folder is the path to the directory which stores the
    # html log and its assiocated images.
    def __init__(self, test_name="",
                 filename=shared_folder + "/error_log",
                 log_folder=shared_folder + "/log"):
        self.file = filename
        self.folder = log_folder
        self.test = test_name
        self.test_failed = False

        self.write("Running...")

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
                self.partial_html = glob_result[0]
            else:
                self.partial_html = self.folder + "/mylog.log"
        
        # Add the CSS stylesheet to the log folder, if it's not there already.
        if not os.path.exists(log_folder + "/log.css"):
            shutil.copyfile(home_folder + "/Integration-Testing-Framework/sikuli/helpers/test_helper.sikuli/log.css",
                            log_folder + "/log.css")

        # Add the display_log script to /vagrant, if it's not there
        # (so it's accessible from the host machine)
        if not os.path.exists(shared_folder + "/display_log.py"):
            shutil.copyfile(home_folder + "/Integration-Testing-Framework/sikuli/helpers/test_helper.sikuli/display_log.py",
                            shared_folder + "/display_log.py")

        doc, tag, text = Doc().tagtext()
        with tag("tr"):
            with tag("td", style="text-align: center; background-color:lightskyblue", colspan="6"):
                text(test_name)
        with open(self.partial_html, "a") as f:
            f.write(doc.getvalue())

    #################################
    # Wrappers for click, type, etc
    #################################

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
            click(thing)
            self.write_html_row("Click", thing, "Success", screenshot)
            if success_message:
                self.write(success_message)
            wait(time)
            return True
        except FindFailed:
            screenshot = capture(SCREEN)
            self.write_fail(fail_message)
            self.write_html_row("Click", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise

    def DoubleClick(self, thing, fail_message, give_up=giveup_default,
                    restart=restart_default,
                    success_message=successmsg_default,
                    time=time_default):
        try:
            screenshot = capture(SCREEN)
            doubleClick(thing)
            self.write_html_row("Double Click", thing, "Success", screenshot)
            if success_message:
                self.write(success_message)
            wait(time)
            return True
        except FindFailed:
            screenshot = capture(SCREEN)
            self.write_fail(fail_message)
            self.write_html_row("Double Click", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False
        except:
            raise

    def Type(self, text, modifiers=0, time=time_default):
        type(text, modifiers)
        wait(time)

    def Find(self, thing, fail_message, give_up=giveup_default,
             restart=restart_default,
             success_message=successmsg_default, time=time_default):
        try:
            screenshot = capture(SCREEN)
            match = find(thing)
            self.write_html_row("Find", thing, "Success", screenshot)
            if success_message:
                self.write(success_message)
            wait(time)
            return match
        except FindFailed:
            screenshot = capture(SCREEN)
            self.write_fail(fail_message)
            self.write_html_row("Find", thing, "Fail", screenshot)
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
            match = wait(thing, wait_time)
            self.write_html_row("Appearance", thing, "Success", screenshot)
            if success_message:
                self.write(success_message)
            wait(time)
            return match
        except FindFailed:
            screenshot = capture(SCREEN)
            self.write_fail(fail_message)
            self.write_html_row("Appearance", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return None
        except:
            raise

    def Exists(self, thing, fail_message, give_up=giveup_default,
               restart=restart_default,
               success_message=successmsg_default):

        screenshot = capture(SCREEN)
        if exists(thing):
            self.write_html_row("Existence", thing, "Success", screenshot)
            if success_message:
                self.write(success_message)
            return True
        else:
            screenshot = capture(SCREEN)
            self.write_fail(fail_message)
            self.write_html_row("Existence", thing, "Fail", screenshot)
            if restart:
                self.restart_flex()
            if give_up:
                exit()
            return False

    def restart_flex(self):
        self.write_fail("Closing and restarting FLEx")
        import restart_flex
        restart_flex.restart_flex()
        exit()

    def get_os(self):
        return self.os

    ###################
    # Logging methods
    ###################

    # Prepends the time and test name and appends a newline before writing to file.
    def write(self, line):
        with open(self.file, "a") as f:
            f.write(time.strftime("%H:%M:%S %x") + " " + self.test + ": " + line + "\n")
        print(time.strftime("%H:%M:%S %x") + " " + self.test + ": " + line + "\n")

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
        
        # Look in all the SIKULI_IMAGE_PATH dirs to see if it's there
        image_dirs = list(getImagePath())
        image_dirs.insert(0, getBundlePath())
        for dir in image_dirs:
            if dir[-1] != '/':
                dir = dir + '/'
            # If found, return the full path
            if os.path.isfile(dir + img):
                return dir + img
    
        return ""

    # Write a log entry into the "mylog.log" file in the log
    # folder, in the form of an html table row (<tr>).
    def write_html_row(self, action_type, expected, result_type, screenshot):
        doc, tag, text = Doc().tagtext()

        # Create the row
        # Test name, Action, Expected, Screenshot
        with tag("tr"):
            if result_type == "Success":
                with tag("td", ('bgcolor', 'green')):
                    text("+++")
            elif result_type == "Fail":
                with tag("td", ('bgcolor', 'red')):
                    text("---")
            else:
                with tag("td"):
                    text("???")
            with tag("td"):
                text(time.strftime("%H:%M:%S %x"))
            with tag("td"):
                text(self.test)
            with tag("td"):
                text(action_type)
            with tag("td"):
                # If 'expected' is given, figure out what kind
                # of thing it is
                if expected:
                    expected_path = ""
                    # If it's a pattern, get the image
                    if isinstance(expected, Pattern):
                        full_path = self.find_valid_image(expected.getFilename())
                        expected_path = self.copy_testfile(full_path)
                    # If it's a match or a region, take a
                    # screenshot of the area
                    elif (isinstance(expected, Match) or
                          isinstance(expected, Region)):
                        screencap = capture(expected)
                        expected_path = self.copy_testfile(screencap)
                    elif isinstance(expected, Location):
                        # Create an area 50px around the location
                        r = Region(expected.getX(), expected.getY(), 0, 0)
                        r = r.nearby()
                        # take a screenshot
                        screencap = capture(r)
                        expected_path = self.copy_testfile(screencap)
                    elif isinstance(expected, str):
                        full_path = self.find_valid_image(expected)

                        # If a path was found, add a clickable image.
                        # If not, add text.
                        if full_path:
                            expected_path = self.copy_testfile(full_path)

                    if expected_path == "":
                        text(expected)
                    else:
                        with tag("a", href="./log/"+expected_path):
                            doc.stag("img", src="./log/"+expected_path)

            with tag("td"):
                screenshot_path = self.copy_testfile(screenshot)
                with tag("a", href="./log/"+screenshot_path):
                    doc.stag("img", src="./log/"+screenshot_path)

        # Write the row to the partial html file
        with open(self.partial_html, "a") as f:
            f.write(doc.getvalue())
