import sys

words = open("words_coded_triangle_number.txt", "r").read().replace('"', "").split(",")

def t(n):
	return int((1/2)*n*(n+1))

triangles = set()

#arbitrary large number
for i in range(1, 1000):
	triangles.add(t(i))

s = 0

for word in words:
	word_value = 0
	for letter in word:
		word_value += ord(letter.lower()) - 96

	if word_value in triangles:
		s += 1

print(s)