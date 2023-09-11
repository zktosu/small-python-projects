import random
words = ["sample","life","boring","stuff","member"]
# words = ["sample"]
word = random.sample(words,1)[0]
res = "-"*len(word)
guesses = 5
while guesses>0:
	letters = input("Enter letters to look for:")
	guesses -= 1
	res = ""
	for i in word:
		if i in letters:
			res += i 
		else:
			res += "-"
	print(res)
	if set(word) == set(res):
		print("Well Done!")
		break
	print("Remaining guesses %d"%guesses)
if guesses <= 0:
	print(word)
	print("Failed")
