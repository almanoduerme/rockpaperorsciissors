import random

def generate_random_number():
    return random.randint(0, 2)

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return options[generate_random_number()]
