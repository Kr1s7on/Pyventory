# Author: Jesalva Kriston Jomari Ballesteros
# Admin No / Grp: 231165R / AA2402

# ┌───────────────────────────────────────────────────┐
# │                                                   │
# │  ____                        _                    │
# │ |  _ \ _   ___   _____ _ __ | |_ ___  _ __ _   _  │
# │ | |_) | | | \ \ / / _ \ '_ \| __/ _ \| '__| | | | │
# │ |  __/| |_| |\ V /  __/ | | | || (_) | |  | |_| | │
# │ |_|    \__, | \_/ \___|_| |_|\__\___/|_|   \__, | │
# │        |___/                               |___/  │
# │                                                   │
# └───────────────────────────────────────────────────┘

# Import necessary modules
import getpass

# File path for passwords
PASSWORDS_FILE = ".passwords.txt"

# ANSI escape code for colors, extra marks for user experience pls
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"

# ANSI escape code to RESET color
RESET = "\033[0m"

def login():
    """
    Perform user login.

    Returns:
        bool: True if login is successful, False otherwise.
    """

    print(YELLOW + "┌───────────────────────────────────────────────────┐" + RESET)
    print(YELLOW + "│                                                   │" + RESET)
    print(YELLOW + "│  ____                        _                    │" + RESET)
    print(YELLOW + "│ |  _ \\ _   ___   _____ _ __ | |_ ___  _ __ _   _  │" + RESET)
    print(YELLOW + "│ | |_) | | | \\ \\ / / _ \\ '_ \\| __/ _ \\| '__| | | | │" + RESET)
    print(YELLOW + "│ |  __/| |_| |\\ V /  __/ | | | || (_) | |  | |_| | │" + RESET)
    print(YELLOW + "│ |_|    \\__, | \\_/ \\___|_| |_|\\__\\___/|_|   \\__, | │" + RESET)
    print(YELLOW + "│        |___/                               |___/  │" + RESET)
    print(YELLOW + "│                                                   │" + RESET)
    print(YELLOW + "└───────────────────────────────────────────────────┘" + RESET)

    username = input("\nEnter username: ")
    password = getpass.getpass("Enter password: ")  # Hide the password input with getpass

    with open(PASSWORDS_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into username and password by : (Wow this is so secure)
            infile_username, infile_password = line.strip().split(':')

        if username == infile_username and password == infile_password:
            print(GREEN + "\nLogin successful!" + RESET)
            return True

    print(RED + "\nAre you even an admin? Invalid username or password.\n" + RESET)
    return False
