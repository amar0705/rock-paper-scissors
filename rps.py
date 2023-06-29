import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    draws = 0
    
    while True:
        print("Rock, Paper, Scissors")
        print("Enter your choice (rock, paper, or scissors), or 'q' to quit:")
        user_choice = input().lower()
        
        if user_choice == 'q':
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)
        
        if user_choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print("Score: User -", user_score, "Computer -", computer_score, "Draws -", draws)
        print()
        
    print("Final Score: User -", user_score, "Computer -", computer_score, "Draws -", draws)
    print("Thanks for playing!")

# Start the game
play_game()
