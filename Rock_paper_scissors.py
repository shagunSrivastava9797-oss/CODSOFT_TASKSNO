import random

CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(CHOICES)


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        else:
            print("Invalid choice. Please type rock, paper, or scissors.")


def decide_winner(user, computer):
    if user == computer:
        return "tie"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if beats[user] == computer:
        return "user"
    else:
        return "computer"


def main():
    print("===== ROCK PAPER SCISSORS =====")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("You won the overall game!")
            elif computer_score > user_score:
                print("Computer won the overall game!")
            else:
                print("Overall game tied!")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
