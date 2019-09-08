def factorial(n):
	factorial = 1
	for i in range (1, n+1):
		factorial = factorial * i
	return factorial

n eh um numero

list(n) sao os numeros separadamente
lista = []
if n == sum(factorial(list(n))):
	lista.append(n)