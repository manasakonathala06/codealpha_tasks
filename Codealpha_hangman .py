
import random

# fruit words
words = ["apple", "mango", "banana", "orange", "grapes"]

word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game - Fruits Edition!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", " ".join(used_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter only!")
        continue

    if guess in used_letters:
        print("You already used that letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the fruit:", word)
else:
    print("\n😢 Game Over! The fruit was:", word)