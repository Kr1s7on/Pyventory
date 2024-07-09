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

"""
GreetUser.py contains the greet_user() function to greet the user based on the current time of day.

The greet_user() function:
    1. gets the current time of day using the datetime module,
    2. greets the user based on the time of day.
"""

# Import the datetime module
import datetime

# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
LIGHT_BLUE = "\033[94m"

# ANSI escape code to RESET color
RESET = "\033[0m"


def greet_user():
    """
    Greets the user based on the current time of day.

    User experience is important.

    Returns:
        A greeting message for the user.
    """

    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 11:
        greeting = GREEN + "\nGood morning!" + RESET

    elif hour < 18:
        greeting = YELLOW + "\nGood afternoon!" + RESET

    else:
        greeting = LIGHT_BLUE + "\nGood evening!" + RESET

    return greeting
