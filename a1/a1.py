fin = open('a1.in')
expenses = fin.readlines()
fin.close()

expenses = map(int, expenses)
expenses.sort()
pivot = 0
start = 1
end = len(expenses) - 1

while (True):
	total = 2020 - expenses[pivot]

	while (expenses[start] + expenses[end] > total):
		end -= 1

	if (expenses[start] + expenses[end] == total):
		print(expenses[pivot], expenses[start], expenses[end], expenses[start] * expenses[end] * expenses[pivot])
		break

	end += 1
	if (start >= end):
		pivot += 1
		start = pivot + 1
		end = len(expenses) - 1
		continue
	start += 1