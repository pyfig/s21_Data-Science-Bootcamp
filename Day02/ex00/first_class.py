class Must_read:
        file = open("data.csv", "r")
        data = file.read()
        file.close()
        print(data)

if __name__ == "__main__":
    Must_read()

