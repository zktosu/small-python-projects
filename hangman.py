import random
# words = ["sample","life","boring","stuff","member"]
words = ["sample"]
word = random.sample(words,1)[0]
res = "-"*len(word)
while True:
	letters = input("Enter a letter:")
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
