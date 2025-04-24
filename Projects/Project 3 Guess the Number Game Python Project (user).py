#Guess the Number Game Python Project (user)
def computer_guesses_number():
    print("🔢 Think of a number between 1 and 100.")
    print("🤫 Don't tell me. Just respond with 'h' (too high), 'l' (too low), or 'c' (correct).")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\nIs your number {guess}?")
        feedback = input("Enter 'h' for too high, 'l' for too low, or 'c' for correct: ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed it in {attempts} attempts!")
            break
        else:
            print("❌ Invalid input. Please enter 'h', 'l', or 'c'.")

# Run the game
computer_guesses_number()
