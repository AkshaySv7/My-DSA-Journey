class ShortPasswordError(Exception):
    pass

def check_password(pwd):
    if len(pwd) < 6:
        raise ShortPasswordError("Password is too short! Must be at least 6 characters.")
    else:
        print("Password accepted.")

try:
    password = input("Enter password: ")
    check_password(password)
except ShortPasswordError as e:
    print(f"Error: {e}")
