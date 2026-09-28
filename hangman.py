import random

# Predefined list of 5 words
words = ["python", "codealpha", "developer", "program", "hangman"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=== Welcome to Hangman Game ===")
print("Guess the word, one letter at a time.")
print(f"You have {max_attempts} incorrect attempts allowed.\n")

while incorrect_guesses < max_attempts:
    # Display the word with guessed letters and underscores
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Current word: " + display_word.strip())
    
    # Check if user has guessed the full word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.\n")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! Attempts remaining: {max_attempts - incorrect_guesses}\n")

if incorrect_guesses == max_attempts:
    print(f"\n❌ Game Over! You ran out of attempts. The word was: '{secret_word}'")