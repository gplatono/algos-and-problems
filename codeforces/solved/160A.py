from sys import stdin

n = int(input())
nums = stdin.readline()
nums = [int(item) for item in nums.split(' ')]

total = sum(nums)
running_sum = 0
count = 0

nums.sort()

for i in range(len(nums)-1, -1, -1):
    running_sum += nums[i]
    count += 1
    if running_sum > int(total / 2):
        break

print(count)
