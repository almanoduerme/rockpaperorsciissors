def get_user_choice():
    while True:
        user_input = input("Select an option! (Rock, Paper, Scissors) or 'quit' to exit: ").strip().capitalize()
        if user_input in ["Rock", "Paper", "Scissors", "Quit"]:
            return user_input
        else:
            print("Invalid selection. Please choose Rock, Paper, or Scissors.")
