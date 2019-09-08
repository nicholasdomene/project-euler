def find_if_prime(n):
    
    for i in range (2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
            break

    return True

def find_primes_under(n):

	primes = []

	i = 2

	while i <= n:
		print (i)
		if find_if_prime(i) is True:
			primes.append(i)
		i = i + 1

	return primes

print(sum(find_primes_under(2000000)))
