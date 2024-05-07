import os
import sys

from scripts.telegram import Telegram
from termcolor import colored

def register_user(telegram):
    username = input("[+] Enter a username ~ ")
    password = input("[+] Enter a password ~ ")
    token = telegram.db.create_user(username, password)
    print(f"Your token is: {token}")

def view_token(telegram):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = telegram.db.get_user(username)
    if user:
        hashed_password = user[1]
        if hashed_password == telegram.db.hash_password(password):
            token = user[2]
            print(f"Your token is: {token}")
        else:
            print(colored("[-] Invalid password.", "red"))
    else:
        print(colored("[-] User not found.", "red"))

def main():
    temp_dir = os.path.join("temp")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    else:
        for file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, file))

    config_file = os.path.join("config.json")

    if not os.path.exists(config_file):
        print(colored("[-] Couldn't not find your config file.", "red"))
        sys.exit(1)

    telegram = Telegram()

    args = sys.argv[1:]

    if len(args) == 0:
        print(colored("[-] No arguments provided.", "red"))
        print("Usage: main.py <command> [arguments]")
        sys.exit(1)

    command = args[0]

    if command == "register":
        register_user(telegram)
        sys.exit(0)
    
    if command == "viewtoken":
        view_token(telegram)
        sys.exit(0)

    if len(args) < 2:
        print(colored("[-] Not enough arguments provided.", "red"))
        print("Usage: main.py <token> <command> [arguments]")
        sys.exit(1)

    token = args[0]
    user = telegram.db.authenticate_user(token)
    if not user:
        print(colored("[-] Invalid token.", "red"))
        sys.exit(1)

    command = args[1]
    command_args = args[2:]

    if command == "upload":
        if len(command_args) < 1:
            print(colored("[-] Not enough arguments provided.", "red"))
            sys.exit(1)

        current_dir = os.getcwd()
        file_path = command_args[0]
        file_name = os.path.basename(file_path)

        if not os.path.exists(file_path):
            print(colored(f"[-] File {file_path} does not exist.", "red"))
            sys.exit(1)

        if os.path.isdir(file_path):
            telegram.upload_directory(current_dir, file_path, file_name, token)
            sys.exit(0)
        else:
            telegram.upload_file(current_dir, file_path, file_name, token)
            sys.exit(0)

    if command == "download":
        if len(command_args) < 1:
            print(colored("[-] Not enough arguments provided.", "red"))
            sys.exit(1)

        file_query = command_args[0]
        telegram.download_file(file_query, token)

        sys.exit(0)

    if command == "list":
        telegram.list_files(token)

        sys.exit(0)

    if command == "remove":
        if len(command_args) < 1:
            print(colored("[-] Not enough arguments provided.", "red"))
            sys.exit(1)

        file_query = command_args[0]
        telegram.remove_file(file_query, token)

        sys.exit(0)

    print(colored(f"[-] Invalid action {command}.", "red"))
    sys.exit(1)


if __name__ == "__main__":
    main()
