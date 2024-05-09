import json
import hashlib
import getpass

logged_in_user = None

def load_pass(username):
    try:
        with open(f"{username}_password.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def saves(passwords, username):
    with open(f"{username}_password.json", "w") as file:
        json.dump(passwords, file)

def create_account():
    global logged_in_user
    username = input("Think of a username: ")
    password = getpass.getpass("And a password to match your account: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    passwords = load_pass(username)
    passwords[username] = {"username": username, "password": hashed_password}
    saves(passwords, username)
    print("Account created successfully!")

def login():
    global logged_in_user
    username = input("Your username: ")
    password = getpass.getpass("Your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    passwords = load_pass(username)
    if username in passwords.keys() and passwords[username]["password"] == hashed_password:
        print("Logged in successfully!")
        logged_in_user = username
    else:
        print("Invalid credentials!")

def load_passwords(username):
    try:
        with open(f"{username}_passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def savess(passwords, username):
    with open(f"{username}_passwords.json", "w") as file:
        json.dump(passwords, file)

def add_password(username):
    global logged_in_user
    if logged_in_user is None:
        print("Please login to add a password.")
        return

    site = input("Enter website or app name: ")
    user=input("Enter user")
    password = input("Enter password: ")
    passwords = load_passwords(username)
    passwords[site] = {"username": user, "password": password}
    savess(passwords, user)
    print("Password saved successfully!")

def retrieve_password():
    global logged_in_user
    if logged_in_user is None:
        print("Please login to retrieve passwords.")
        return

    site = input("Enter website or app name: ")
    passwords = load_passwords(logged_in_user)
    if site in passwords:
        print("Username:", passwords[site]["username"])
        print("Password:", passwords[site]["password"])
    else:
        print("Password not found for", site)

def main():
    global logged_in_user
    if logged_in_user is None:
        print("Please login to continue.")
        return False

    print("\n1. Add a password")
    print("2. Retrieve a password")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_password(logged_in_user)
    elif choice == "2":
        retrieve_password()
    elif choice == "3":
        print("Exiting...")
        return False  # Indicate to exit the loop
    else:
        print("Invalid choice. Please try again.")
    return True  # Continue running the loop

def app():
    global logged_in_user

    while True:
        if logged_in_user:
            if not main():
                break
        else:
            print("\n1. Create an account")
            print("2. Login")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                create_account()
            elif choice == "2":
                login()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

app() 
