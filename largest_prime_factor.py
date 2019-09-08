def factors(n):

	factors=[]
	i = 1
	tempn = n
	while i <= tempn:
		if n%i == 0:
			factors.append(i)
		tempn = n / i
		i = i + 1
	return factors

print(factors(600851475143))