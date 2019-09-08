def palindrome(n):

	list = []

	for digit in str(n):
		list.append(digit)
	try:
		if list[0] == list[5]:
			if list[1] == list [4]:
				if list [2] == list [3]:
					return True
	except IndexError:
		if len(list) == 5:
			if list[0] == list[4]:
				if list[1] == list [3]:
					return True
		if len(list) == 4:
			if list[0] == list [3]:
				if list [1] == list [2]:
					return True
	return False


def trials():

	i = 999
	t = 999
	palindromes = []

	for trial in range(1000000):
		if palindrome(i*t) == True:
			palindromes.append(i*t)
		t = t - 1
		if t == 101:
			t = 999
			i = i - 1

	print (max(palindromes))


trials()



