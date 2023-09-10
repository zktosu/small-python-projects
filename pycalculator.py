
while True:
	operation = input("select operation(+-/*): ")
	if operation == '+':
		number1 = input("number 1 please:")
		number2 = input("number 2 please:")
		res = number1 + number2
	if operation == '-':
		number1 = input("number 1 please:")
		number2 = input("number 2 please:")
		res = number1 - number2
	if operation == '/':
		number1 = input("number 1 please:")
		number2 = input("number 2 please:")
		res = number1 / number2
	if operation == '*':
		number1 = input("number 1 please:")
		number2 = input("number 2 please:")
		res = number1 * number2
	if operation == "q":
		break
	print(res)
