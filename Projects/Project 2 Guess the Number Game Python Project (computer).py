import random

def guess_the_number():
    print("🎲 Welcome to 'Guess the Number' Game!")
    print("I'm thinking of a number between 1 and 100...")
    print("Type 'exit' to quit the game at any time.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Take a guess: ")

        if user_input.lower() == "exit":
            print("👋 Game exited. Thanks for playing!")
            break

        try:
            guess = int(user_input)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number or 'exit' to quit.")

guess_the_number()
