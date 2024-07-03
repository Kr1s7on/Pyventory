# Author: Jesalva Kriston Jomari Ballesteros
# Admin No / Grp: 231165R / AA2402

"""
┌───────────────────────────────────────────────────┐
│                                                   │
│  ____                        _                    │
│ |  _ \ _   ___   _____ _ __ | |_ ___  _ __ _   _  │
│ | |_) | | | \ \ / / _ \ '_ \| __/ _ \| '__| | | | │
│ |  __/| |_| |\ V /  __/ | | | || (_) | |  | |_| | │
│ |_|    \__, | \_/ \___|_| |_|\__\___/|_|   \__, | │
│        |___/                               |___/  │
│                                                   │
└───────────────────────────────────────────────────┘
"""

# Import necessary modules
import getpass

# File path for passwords
PASSWORDS_FILE = ".passwords.txt"

def login():
    """
    Perform user login.

    Returns:
        bool: True if login is successful, False otherwise.
    """

    # ANSI escape code for colors, extra marks for user experience pls
    yellow_gold_text = "\033[93m"
    green_text = "\033[92m"
    red_text = "\033[91m"

    # ANSI escape code to reset color
    reset = "\033[0m"

    print(yellow_gold_text + "┌───────────────────────────────────────────────────┐" + reset)
    print(yellow_gold_text + "│                                                   │" + reset)
    print(yellow_gold_text + "│  ____                        _                    │" + reset)
    print(yellow_gold_text + "│ |  _ \\ _   ___   _____ _ __ | |_ ___  _ __ _   _  │" + reset)
    print(yellow_gold_text + "│ | |_) | | | \\ \\ / / _ \\ '_ \\| __/ _ \\| '__| | | | │" + reset)
    print(yellow_gold_text + "│ |  __/| |_| |\\ V /  __/ | | | || (_) | |  | |_| | │" + reset)
    print(yellow_gold_text + "│ |_|    \\__, | \\_/ \\___|_| |_|\\__\\___/|_|   \\__, | │" + reset)
    print(yellow_gold_text + "│        |___/                               |___/  │" + reset)
    print(yellow_gold_text + "│                                                   │" + reset)
    print(yellow_gold_text + "└───────────────────────────────────────────────────┘" + reset)

    username = input("\nEnter username: ")
    password = getpass.getpass("Enter password: ")  # Hide the password input with getpass

    with open(PASSWORDS_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into username and password by : (Wow this is so secure)
            stored_username, stored_password = line.strip().split(':')

        if username == stored_username and password == stored_password:
            print(green_text + "\nLogin successful!" + reset)
            return True

    print(red_text + "\nAre you even an admin? Invalid username or password.\n" + reset)
    return False
