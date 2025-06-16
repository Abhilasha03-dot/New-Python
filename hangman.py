import random

# Predefined word list
words = ["apple", "banana", "mango", "grape", "peach"]

# Pick a random word
secret_word = random.choice(words)

# Game setup
guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", attempts_left, "incorrect guesses allowed.\n")

# Game loop
while attempts_left > 0 and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print("Guessed letters: ", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Enter a single letter only.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

# Result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
