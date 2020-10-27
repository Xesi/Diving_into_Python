class FileReader:

    def __init__(self, path):
        self._path = path

    def read(self):
        try:
            with open(self._path) as file:
                return file.read()

        except FileNotFoundError:
            return str()
