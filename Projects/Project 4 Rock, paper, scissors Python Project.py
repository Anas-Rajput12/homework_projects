#Rock, paper, scissors Python Project
import random

def play_rps():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    options = ['rock', 'paper', 'scissors']

    while True:
        user = input("\nChoose rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user == 'exit':
            print("👋 Thanks for playing!")
            break

        if user not in options:
            print("❌ Invalid choice. Try again.")
            continue

        computer = random.choice(options)
        print(f"🧠 Computer chose: {computer}")

        if user == computer:
            print("🤝 It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

# Start the game
play_rps()
