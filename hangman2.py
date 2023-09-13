# show secret word with dashes (-)
# get a letter from user (a letter)
# check if letter is gussed already
# add letter to guessed letters list
# update dashed word. replace - for correct letters.
# loop
import random
words = ["word","life","another","member","other"]
word = random.sample(words,1)[0]
dword = "-"*len(word)
guessed_letters = ""
def update_word():
	global words
	global word
	global dword
	global guessed_letters
	word = random.sample(words,1)[0]
	dword = "-"*len(word)
	guessed_letters = ""
while True:
	print(word)
	print(dword)
	letter = input("Give me a letter: ")
	if len(letter) != 1 or letter in guessed_letters:
		print("Error, letter used or you have given too much")
		continue
	guessed_letters += letter
	for i in range(len(word)):
		if letter == word[i]:
			# this is the way to replace dash with letter
			dword = dword[:i] + letter + dword[i+1:]
	if dword == word:
		print("Well Done!")
		print(dword)
		update_word()
	# this needs to be replaced with geniune solution
	# wrong gusses need to be counted
	if len(guessed_letters) == len(word):
		print("You have used all guesses")
		break

