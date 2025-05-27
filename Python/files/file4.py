# filter_keyword.py
source_file = "sample.txt"
target_file = "filtered.txt"
keyword = input("Enter keyword to search: ")

try:
    with open(source_file, 'r') as sf, open(target_file, 'w') as tf:
        for line in sf:
            if keyword in line:
                tf.write(line)
    print(f"Lines containing '{keyword}' written to {target_file}")
except FileNotFoundError:
    print("Source file not found.")
