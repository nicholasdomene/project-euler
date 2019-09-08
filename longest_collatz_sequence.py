chain = [[], []]

i = 2

while i <= 1000000:
	n = i
	print("i é", i)
	templist = []
	chain.append(templist)
	while n != 1:
		if n%2 ==0:	
			n = n/2
			chain[i].append(n)
		else:
			n = 3*n + 1
			chain[i].append(n)
	chain[i].append(n)
	i = i+1

lens = []
for i in range(1000001):
	lens.append(len(chain[i]))

print(lens.index(max(lens)))

