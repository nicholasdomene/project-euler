def fib(n):

	if (n == 0 or n == 1):
		result = 1

	else:
		result = fib(n-1) + fib(n-2)



	return result

def fib_list(n):

	fib_list = []

	for i in range (n):
		fib_list.append(fib(i))

	return fib_list

def even_fib(n):

	fibo_list = fib_list(n)
	even_fib_list = []

	for fib in fibo_list:
		if fib <= 4000000 and fib%2 ==0:
			even_fib_list.append(fib)

	return even_fib_list

print(sum(even_fib(33)))




