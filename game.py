def play_round(get_user_choice, get_computer_choice):
    user_select = get_user_choice()
    if user_select == "Quit":
        return None  # Indicates the user wants to quit

    computer_select = get_computer_choice()
    print(f"Computer selected: {computer_select}")
    print(f"You selected: {user_select}")

    if user_select == computer_select:
        print("It's a tie!")
        return 0, 0
    elif (user_select == "Rock" and computer_select == "Scissors") or \
         (user_select == "Paper" and computer_select == "Rock") or \
         (user_select == "Scissors" and computer_select == "Paper"):
        print("You win!")
        return 1, 0  # User wins
    else:
        print("You lose!")
        return 0, 1  # Computer wins
