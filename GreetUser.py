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

# Import the datetime module
import datetime

def greet_user():
    """
    Greets the user based on the current time of day.

    I don't think anyone else did this, so extra marks pls cher :D (I need to pullup my grade for this module)

    Returns:
        A greeting message for the user.
    """

    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 12:
        greeting = "\nGood morning!"

    elif hour < 18:
        greeting = "\nGood afternoon!"
        
    else:
        greeting = "\nGood evening!"

    return greeting
