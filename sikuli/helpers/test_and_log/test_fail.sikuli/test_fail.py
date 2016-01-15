from __future__ import with_statement
from sikuli import *
import os
import shutil
import yattag_templates.one_fail

class TestFail:

    def _copy_files(self, files):
        # Copy the files
        copied_files = []
        for file in files:
            if file is not None:
                name = os.path.basename(file) 
                shutil.copyfile(file, self.folder + name)
                copied_files.append(name)
            else:
                copied_files.append(None)

        return copied_files

    def __init__(self, path):
        """
        Create a TestFail object associated with a file.
        :param path: Name or path of a file. The file will be created if it does not exist,
        otherwise any future new entries will be appended.
        :return: A new TestFail associated with the given file.
        """
        # Create the directory
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise
        self.folder = path
        self.log = path + "log.html"

    def clicked_fail(self, clicked_image, expected_screen=None, screencap=None):
        # Copy image files to the specified path
        copied_files = self._copy_files([clicked_image, expected_screen, screencap])
            
        with open(self.log, "a") as f:
            t = yattag_templates.one_fail.template(
                    copied_files[0], copied_files[1], copied_files[2]).getvalue()
            f.write(t)

    def img_find_fail(self, expected_image, expected_screen=None, region=None):
        """
        Add an entry to the failed tests file. To be used when an expected image was not found
        on the screen or in a certain region.
        :param expected_image: The image Sikuli was looking for on the screen.
        :param expected_screen: What the entire screen was expected to look like.
        :param region: The region the image was to be found in, if applicable.
        """
        pass

    def change_fail(self, region, expected=None):
        """
        Add an entry to the failed tests file. To be used when there should have been a change
        in a region of the screen.
        :param region: The region where a change was supposed to occur.
        :param expected:
        """
        pass
