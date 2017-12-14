import sys


class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            file = open(self.file_path, 'r')
            return print(file.read())
        except IOError:
            return ""


reader = FileReader("README.md")
print(reader.read())