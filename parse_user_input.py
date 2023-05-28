# Filename: parse_user_input.py

def parse_user_input():
    while True:
        user_input = input('> ')
        user_input = user_input.strip()
        if validate_user_input(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_user_input(user_input):
    # Add validation logic here
    # For example, check if the user input is not empty
    if user_input:
        return True
    else:
        return False
