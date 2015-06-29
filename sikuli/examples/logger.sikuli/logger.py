from __future__ import with_statement

# So we don't have to define a write_log function in every test file :P
class Logger:
    # If a file with the given filename already exists, the Logger will
    # just keep writing to the end of that file.
    def __init__(self, test_name="", filename="/vagrant/error_log"):
        self.file = filename
        self.test = test_name + ": "

    # Prepends the test name and appends a newline before writing to file.
    def write(self, line):
        with open(self.file, "a") as f:
            f.write(self.test + line + "\n")