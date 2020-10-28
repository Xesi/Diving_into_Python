import os
import uuid


class File:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.current_position = 0
        with open(path_to_file, 'w'):
            pass

    def read(self):
        with open(self.path_to_file, 'r') as file:
            return file.read()

    def write(self, content):
        with open(self.path_to_file, 'w') as file:
            file.write(content)

    def __add__(self, rhs):
        new_path = os.path.join(
            os.path.dirname(self.path_to_file),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + rhs.read())

        return new_file

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to_file, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line
