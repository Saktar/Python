word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

guess = input("Guess a letter: ")

while True:
	if(guess in word):
		print("Correct!")
		break
	else:
		print("Wrong! Try again.")
		break




# Some useful variables
guesses = []
maxfails = 7

from random
