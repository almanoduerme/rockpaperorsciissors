from game import play_round
from user import get_user_choice
from computer import get_computer_choice

def main():
    user_score = 0
    computer_score = 0

    for _ in range(10):
        round_result = play_round(get_user_choice, get_computer_choice)
        if round_result is None:
            print("Thank you for playing!")
            break
        user_score += round_result[0]
        computer_score += round_result[1]
        print(f"Scores - You: {user_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    main()
