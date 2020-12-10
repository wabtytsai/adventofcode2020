fin = open("a9.in")

nums = list(map(int, fin.readlines()))

n = len(nums)

def find(nums, preamble):
	for i in range(n - preamble - 1):
		last = nums[i: i + preamble]
		valid = False
		for num in last:
			diff = nums[i + preamble] - num
			if diff != num and diff in last:
				valid = True
				break
		if not valid:
			return nums[i + preamble]

def add(nums, target):
	low = 0
	total = nums[0] + nums[1]
	for high in range(2, len(nums)):
		total += nums[high]
		while total > target:
			total -= nums[low]
			low += 1
		if total == target:
			link = nums[low: high + 1]
			return (min(link) + max(link))

target = find(nums, 25)
print(target)
print(add(nums, target))
fin.close()
