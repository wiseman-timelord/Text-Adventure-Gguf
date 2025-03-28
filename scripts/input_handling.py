# Filename: data/scripts/input_handling.py
import re

def parse_user_input():
    while True:
        user_input = input("> ").strip()
        if re.match(r'^[\w\s,.!?]+$', user_input):
            return user_input
        print("Invalid input! Use only letters/numbers.")