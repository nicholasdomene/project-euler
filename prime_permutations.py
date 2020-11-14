def is_prime(n):
	for prime in primes:
		if n%prime == 0:
			return False
	primes.add(n)
	return True

primes = set([2])

for i in range(3, 10000, 2):
	#create set of all primes until 10,000
	is_prime(i)

def permutation(n):
	first_digit = n//1000
	if first_digit == 0: return 
	three_digits = n%(first_digit*1000)
	return int(str(three_digits) + str(first_digit))

def solution():
	delta = 3330
	base_case = 1487
	for i in range(1001, 9999, 2):
		if i in primes:
			print(set(list(str(i))))
			#if i is prime, check permutation
			if i + delta in primes:
				if i + 2*delta in primes:
					if set(list(str(i))) == set(list(str(i+delta))) == set(list(str(i+2*delta))):
						if i != base_case:
							return str(i) + str(i+delta) + str(i+2*delta)

print(solution())