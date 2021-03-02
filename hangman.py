import random 
from words import words
import string

def get_valid_word(words):
	word = random.choice(words)  # randomly chooses something from the list
	# we don't want dashes or spaces in word coz it will we unable for python to enter dashes or spaces 
	# this loop will iterate till we get a valid word
	while '-' in word or ' ' in words:
		word = random.choice(words)	

	return word.upper()


# keeping track of which letters we've guessed
# and which letters in the word we've correctly guessed
def hangman():
	word = get_valid_word(words)
	# A variable that saves all the letters in a word as a set
	# so this variable keeps track of what letter has been guessed in the word
	word_letters = set(word)  # letters in  the word
	alphabet = set(string.ascii_uppercase)
	used_letters = set()  # what the user has guessed

	lives = 6

	#getting user input
	while len(word_letters) > 0 and lives > 0:
		# letters used
		# ' '.join(['a', 'b', 'cd']) --> 'a b cd'
		print("\nYou have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))


		# telling the user what the current word is (ie, W - R D)
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print("Current word: ", ' '.join(word_list))

		user_letter = input("Guess a letter: ").upper()

		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
				print('')

			else:
				lives -= 1  # takes away a life if wrong
				print("Letter is not in word.")

		elif user_letter in used_letters:
			print("\nYou have already used that character. Please try again.")

		else:
			print("\nInvalid character. Please try again.")

	# gets here when len(word_letters) == 0 OR when lives == 0
	if lives == 0:
		print("You died, sorry, The word was", word)
	else:
		print("CONGRATULATIONS!!, You guessed the word", word, '!!')


# user_input = input("Type Something: ")
# print(user_input)


if __name__ == '__main__':
	hangman()