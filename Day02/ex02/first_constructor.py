import sys
import os


# python3 first_constructor.py ../ex01/data.csv
class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        file = open(self.path, "r")
        data = file.read()
        file.close()
        print(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide a path to the file as an argument.")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("Error: The file does not exist.")
        sys.exit(1)
    Research(sys.argv[1]).file_reader()