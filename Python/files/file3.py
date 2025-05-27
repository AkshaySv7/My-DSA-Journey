# write_user_input.py
filename = "user_input.txt"

with open(filename, 'w') as file:
    print("Enter 5 lines of text:")
    for i in range(5):
        line = input(f"Line {i+1}: ")
        file.write(line + "\n")

print("Data written to file successfully.")
