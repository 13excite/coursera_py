import os
import tempfile


class File():

    def __init__(self, filename):
        self.filename = filename

    def __add__(self, other):
        with open(self.filename, 'r') as file_one, open(other.filename, 'r') as file_two:
            data = file_one.read() + file_two.read()
            new_obj = File(os.path.join(tempfile.gettempdir(), 'new'))
            new_obj.write(data)
            return new_obj

    def __getitem__(self, item):
        with open(self.filename, 'r') as file:
            data = file.readlines()
            return data[item].strip()

    def __repr__(self):
        return '%s' % self.filename

    def write(self, string):
        with open(self.filename, 'w') as f:
            f.write(string)


obj = File('/tmp/file.txt')

obj.write('line\n')

first = File('/tmp/first')
second = File('/tmp/second')

new_obj = first + second
print(new_obj)

obj_test = File('/tmp/file.txt')

print(obj_test)