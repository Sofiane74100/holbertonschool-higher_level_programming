def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

# Example usage:
# read_file("my_file_0.txt")
