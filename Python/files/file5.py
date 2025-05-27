
# note_app.py
filename = "notes.txt"

print("Simple Note-Taking App")
while True:
    note = input("Enter your note (or type 'exit' to quit): ")
    if note.lower() == 'exit':
        break
    with open(filename, 'a') as file:
        file.write(note + "\n")

print("Notes saved.")
