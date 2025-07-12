import random

word_list = ['apple', 'house', 'pizza', 'light', 'train']

secret_word = random.choice(word_list)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

display_word = ['_' for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word by entering one letter at a time.")
print(f"You have {max_guesses} incorrect guesses allowed.")
print("Word to guess: " + ' '.join(display_word))

while incorrect_guesses < max_guesses and '_' in display_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} tries left.")

    print("Word: " + ' '.join(display_word))
    print("Guessed letters: " + ', '.join(guessed_letters))
    print()

# Final outcome
if '_' not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game over! The word was:", secret_word)