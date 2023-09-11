import random
words = ["sample","life","boring","stuff","member"]
word = random.sample(words,1)[0]
res = "-"*len(word)
while True:
	letter = input("Enter a letter:")
	res = ""
	for i in word:
		if i == letter:
			res += letter
		else:
			res += "-"
	print(res)
