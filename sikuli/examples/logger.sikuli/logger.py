from __future__ import with_statement

# So we don't have to define a write_log function in every test file. :P
# If write_fail is used instead of write, the logger remembers that the
# test failed.
class Logger:
    # If a file with the given filename already exists, the Logger will
    # just keep writing to the end of that file.
    def __init__(self, test_name="", filename="/vagrant/error_log"):
        self.file = filename
        self.test = test_name + ": "
        self.test_failed = False

    # Prepends the test name and appends a newline before writing to file.
    def write(self, line):
        with open(self.file, "a") as f:
            f.write(self.test + line + "\n")

    # Same as write, but internally remembers that the test failed.
    def write_fail(self, line):
        self.test_failed = True
        self.write(line)

    # Returns whether any fails have been logged.
    def has_fail(self):
        return self.test_failed