def multiple(n):

	mult = 0

	for i in range (11, 20):
		if n%i != 0:
			return False

	return True

def find():

	i = 222544020

	while multiple(i) is False:
		print(i)
		i = i + 20
	print (i)

find()

#232792560
#demorou muito, mas funcionou