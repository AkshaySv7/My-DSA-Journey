class LoginError(Exception):
    pass

def login(user, passwd):
    correct_user = "admin"
    correct_pass = "123456"
    if user != correct_user or passwd != correct_pass:
        raise LoginError("Incorrect username or password!")
    else:
        print("Login successful.")

try:
    username = input("Username: ")
    password = input("Password: ")
    login(username, password)
except LoginError as e:
    print(f"Login failed: {e}")
