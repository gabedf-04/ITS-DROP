class GestoreFile:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self, filename):
        righe = []
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip().split(";")
                righe.append(line)
        return righe
    def write_file(self, filename, data):
        with open(self.filename, "a") as file:

