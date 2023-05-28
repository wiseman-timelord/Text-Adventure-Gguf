import re

def parse_user_input():
    while True:
        user_input = input('> ')
        user_input = user_input.strip()
        user_input = re.split(r'\s+', user_input)
        if validate_user_input(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_user_input(user_input):
    # Add validation logic here
    pass