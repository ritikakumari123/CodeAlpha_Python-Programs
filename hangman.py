import random

# list of words
words = ["apple", "mango", "tiger", "table", "chair"]

# choose one word randomly
word = random.choice(words)

# to store guessed letters
guessed_letters = []

# number of chances
chances = 6

# create blank word like _ _ _ _
display = []

for i in word:
    display.append("_")

print("Welcome to Hangman Game!")

# game loop
while chances > 0:

    print("\nWord:", " ".join(display))
    print("Chances left:", chances)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ")
    guess = guess.lower()

    # check if already guessed
    if guess in guessed_letters:
        print("You already tried this letter.")
        continue

    guessed_letters.append(guess)

    # check if guess is correct
    if guess in word:
        print("Good guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        print("Wrong guess!")
        chances = chances - 1

    # check if word is completed
    if "_" not in display:
        print("\nYou won! The word is:", word)
        break

# if user loses
if "_" in display:
    print("\nYou lost! The word was:", word)
