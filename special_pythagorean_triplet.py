def pythagorean():


	for i in range(1, 1000):
		for j in range(2, 1000):
			for k in range(3, 1000):
				if i**2 + j**2 == k**2:
					print (i, j, k)
					if i+j+k == 1000:
						print (i)
						print (j)
						print (k)
						quit()


pythagorean()
