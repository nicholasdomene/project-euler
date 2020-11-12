import datetime

t1 = datetime.datetime.now()

def is_prime(n):
		if n in primes:
			return True
		for prime in primes:
			if n%prime==0:
				return False
		#assuming a prior set of primes all smaller than n,		
		#if n is not divisible by any other prime smaller than itself, it is a prime
		return True

#create set with every prime until an arbitrary large number (10,000)
primes = set([2])
for i in range(3, 10000, 2):
	if is_prime(i):
		primes.add(i)

def concatenate_two_numbers(x, y):
	return int(str(x) + str(y))

def is_remarkable(x, y):
	if is_prime(concatenate_two_numbers(x, y)) and is_prime(concatenate_two_numbers(y, x)):
		return True
	else:
		return False

def find_solution():
	#since every number ending with 2, we can start with 3 
	list_primes = sorted(list(primes))[3:]

	for i in range(0, len(list_primes)-4):
		for j in range(i+1, len(list_primes)-3):
			#check if pair is remarkable
			if is_remarkable(list_primes[i], list_primes[j]):
				for k in range(j+1, len(list_primes)-2):
					#check if new number is remarkable with all previous ones
					if is_remarkable(list_primes[i], list_primes[k]) and is_remarkable(list_primes[j], list_primes[k]):
						for l in range(k+1, len(list_primes)-1):
							#check if new number is remarkable with all previous ones
							if is_remarkable(list_primes[i], list_primes[l]) and is_remarkable(list_primes[j], list_primes[l]) and is_remarkable(list_primes[k], list_primes[l]):
								for m in range(l+1, len(list_primes)):
									#check if new number is remarkable with all previous ones
									if is_remarkable(list_primes[i], list_primes[m]) and is_remarkable(list_primes[j], list_primes[m]) and is_remarkable(list_primes[k], list_primes[m]) and is_remarkable(list_primes[l], list_primes[m]):
										return list_primes[i] + list_primes[j] + list_primes[k] + list_primes[l] + list_primes[m]
		

solution = find_solution()

t2 = datetime.datetime.now()
print("The solution is ", solution)
print("Time to run: ", str(t2 - t1))
