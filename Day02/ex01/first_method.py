class Research:
    def file_reader(self):
        file = open("data.csv", "r")
        data = file.read()
        file.close()
        print(data)

if __name__ == "__main__":
    Research().file_reader()