birthdays = {
    "akshay": "Jan 5",
    "alan": "Feb 10",
    "amal": "Mar 15",
    "nandu": "Apr 20",
    "saran": "May 25"
}

name = input("Enter a friend's name to search their birthday: ")
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}")
else:
    print("Name not found.")
