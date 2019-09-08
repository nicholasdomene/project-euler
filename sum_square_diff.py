def sum_naturals(n):


	sum_natural = 0

	for i in range (1, n):
		sum_natural = sum_natural + i
	return (sum_natural**2)
def sum_squares(n):
	sum_square = 0
	for i in range (1, n):
		sum_square = sum_square + (i**2)
	return sum_square

def diff(n):

	sum1 = sum_squares(n)
	sum2 = sum_naturals(n)

	difference = sum1 - sum2
	print(difference)

diff(100)