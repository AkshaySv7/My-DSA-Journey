# read_and_print.py
filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        contents = file.read()
        print("File Contents:\n")
        print(contents)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
