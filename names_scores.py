names = open('names_scores_input.txt', 'r')

names = list(names)

names[0] = names[0].replace('"', '')

names = list(names[0].split(','))

names = sorted(names)

alphabet = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

s = 0

for name in range(len(names)):
	name_score = 0
	letters = names[name]
	letters = list(letters)
	print(letters)
	for letter in letters:
		name_score += alphabet.index(letter)
		print(alphabet.index(letter))
	s += name_score * (name + 1)

print("The total is %s"%s)
