fin = open('a1.in')
expenses = fin.readlines()
fin.close()

expenses = list(map(int, expenses))

def two_sum(numbers):
	sorted_numbers = sorted(numbers)
	end = len(sorted_numbers) - 1
	for start in range(len(sorted_numbers)):
		while sorted_numbers[start] + sorted_numbers[end] > 2020:
			end -= 1
		if end <= start:
			break
		if sorted_numbers[start] + sorted_numbers[end] == 2020:
			return sorted_numbers[start] * sorted_numbers[end]
	return -1

def three_sum(numbers):
	sorted_numbers = sorted(numbers)
	for z in range(len(sorted_numbers)):
		new_sum = 2020 - sorted_numbers[z]
		end = len(sorted_numbers) - 1
		for start in range(z + 1, len(sorted_numbers)):
			while sorted_numbers[start] + sorted_numbers[end] > new_sum:
				end -= 1
			if end <= start:
				break
			if sorted_numbers[start] + sorted_numbers[end] == new_sum:
				return sorted_numbers[start] * sorted_numbers[end] * sorted_numbers[z]
	return -1

print(two_sum(expenses))
print(three_sum(expenses))