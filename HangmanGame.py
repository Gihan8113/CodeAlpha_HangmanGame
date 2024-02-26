# import random module for genarating random number
import random

# create ASCII art representation for hangman game
hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / 
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / \
"""
]


# list of lowercase animal names that the player needs to guess
animals = ['tiger', 'lion', 'giraffe', 'zebra', 'dolphin', 'shark', 'elephant', 'rhino']

#  Selecting a random word from the list and converting it to lowercase
word = random.choice(animals).lower()

guessed_correctly = []    # List to store correctly guessed letters
guessed_incorrectly = []  # List to store incorrectly guessed letters
tries = 6                 # Number of allowed guesses
hangman_count = -1        # Variable to track the number of incorrect guesses

# Create loop for game guessing
while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ '
    if output == word:
        break

    # Print the current state of the word
    print("Guess the word: ",output)

    # Print the number of remaining chances
    print(tries," chances left")

    # Prompt the player to enter a guess and convert it to lowercase
    guess = input().lower()


# Check user's guess and printing feedback
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in word:
        print("Awesome Job! You guessed the correct letter!")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You have guessed a wrong letter!")
        hangman_count = hangman_count + 1
        tries = tries-1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])            # Print the corresponding hangman figure

# If the player has remaining tries, they have guessed the word correctly
if tries>0:
    print("You guessed it right and you win!!!")
else:
    print("Sorry you guessed the wrong letter. Try again.")

