# Basic login

users_database = {}

def signup():
    print("--- Signup ---")
    while True:
        new_user = input("Enter yor name: ")
        if new_user in users_database:
            print(f"This username '{new_user}' already exists.")
        else:
            new_password = input("Enter your password: ")
            users_database[new_user] = new_password
            print(f"Successfully registered.\n")
            break

def login():
    print("--- Login ----")
    if not users_database:
        print("User not found.\n")
        return

    user = input("Enter your user: ")
    password = input("Enter yor password: ")

    if user in users_database and users_database[user] == password:
        print(f"Welcome, '{user}'!\n")
    else:
        print("Incorrect username or password!\n")

def main():
    while True:
        print("--- Main menu ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        option = input("Enter on option (1-3): ")

        if option == '1':
            signup()
        elif option == '2':
            login()
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option.")
main()