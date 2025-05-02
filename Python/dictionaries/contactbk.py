contacts = {}

while True:
    print("\n1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")
    elif choice == "2":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}'s number is {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
