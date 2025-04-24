import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'code']
    word = random.choice(words)
    guessed = "_" * len(word)
    guessed_letters = []
    attempts = 6  # Number of allowed wrong guesses

    print("🎯 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("Type 'exit' to quit the game anytime.")
    print(f"You have {attempts} chances.\n")

    while attempts > 0 and "_" in guessed:
        print("Word:", ' '.join(guessed))
        print("Guessed letters:", ', '.join(guessed_letters))
        guess = input("Enter a letter (or 'exit' to quit): ").lower()

        if guess == 'exit':
            print("👋 Thanks for playing! Goodbye!")
            break

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!\n")
            guessed = ''.join([letter if letter == guess or guessed[i] != "_" else "_"
                               for i, letter in enumerate(word)])
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

    if "_" not in guessed:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    elif attempts == 0:
        print(f"💀 Game Over! The word was: {word}")

# Run the game
hangman()
