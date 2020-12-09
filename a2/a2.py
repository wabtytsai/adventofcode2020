fin = open('a2.in')
total = 0

for line in fin.readlines():
	freq, letter, password = line.split(' ')
	low, high = map(int, freq.split('-'))
	letter = letter[0]
	password.strip()
	password = " " + password

	count = 0
	if (password[low] == letter):
		count += 1
	if (password[high] == letter):
		count += 1
	if (count == 1):
		total += 1
print total
