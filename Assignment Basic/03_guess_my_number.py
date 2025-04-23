import random

def guess_my_number():
    secret_number = random.randint(0, 99)
    print("Guess My Number")
    print("I am thinking of a number between 0 and 99...")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("Enter a guess: ")

        if user_input.lower() == "exit":
            print("Game exited. Better luck next time!")
            break

        # Convert the input to int only if it's not "exit"
        guess = int(user_input)

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

# Run the game
guess_my_number()
