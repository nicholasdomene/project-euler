def multiples(n):

	sum_of_multiples = 0

	i = 1

	for i in range(n):
		if (i%3 == 0 or i%5 ==0):
			sum_of_multiples = sum_of_multiples + i
			print (i)
			i += 1
		
	return sum_of_multiples

print (multiples(1000))
