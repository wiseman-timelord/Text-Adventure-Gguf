# Filename: parse_user_input.py
import re

def parse_user_input():
    while True:
        user_input = input('> ')
        user_input = user_input.strip()
        if validate_user_input(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_user_input(user_input):
    # Check if the user input is not empty and contains only alphanumeric characters and spaces
    if user_input and re.match('^[a-zA-Z0-9 ]*$', user_input):
        return True
    else:
        return False
