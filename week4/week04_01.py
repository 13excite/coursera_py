import os
import tempfile


class File():

    def __init__(self, filename):
        self.filename = filename

    def __add__(self, other):
        pass

    def __getitem__(self, item):
        with open(self.filename, 'r') as file:
            data = file.readlines()
            return data[item].strip()

    def __repr__(self):
        return '%s' % self.filename

    def write(self, string):
        pass