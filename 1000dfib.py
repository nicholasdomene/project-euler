fib = [1, 1]

j = 2

while True:
	new = fib[j-1] + fib[j-2]
	if len(str(new)) != 1000:
		fib.append(new)
		print(j)
		j += 1
	else:
		print (j)
		break
