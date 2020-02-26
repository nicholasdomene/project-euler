def is_prime(n):
    for i in range(2, n):
        if n%i == 0: return False
    return True

results = []

for a in range(-1000, 1001):
    for b in range(0, 1001):
        if is_prime(b) is True:
            n = 1
            while (n*n + a*n + b)>0 and  is_prime(n*n + a*n + b) is True:
                n += 1
            print((a, b, n))
            results.append((a, b, n))

max_prime = max(i[2] for i in results)

print("Max quantity of primes generated was %s"%max_prime)

for i in results:
    if i[2] == max_prime:
        print(i)
        print("The product of the coefficients is %s"%(i[0]*i[1]))
