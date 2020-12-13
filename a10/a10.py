fin = open("a10.in")

nums = list(map(int, fin.readlines()))
nums.sort()

one = 0
three = 0

last = 0
for num in nums:
    diff = num - last
    if diff == 1:
        one += 1
    if diff == 3:
        three += 1
    last = num

print (one, three + 1)

dp = [0] * (max(nums) + 1)
dp[0] = 1

for num in nums:
    dp[num] = sum(dp[max(num - 3, 0): num])

print(dp[-1])

fin.close()
