import sys


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path


    def read(self, path):
        with open(path) as f:
            f.read()
            f.close()
        pass
