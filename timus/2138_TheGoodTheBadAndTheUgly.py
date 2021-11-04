import sys

flag = input()
num = int(input())

if num == 0:
	print(0)
	sys.exit()

digits = [0] * 4
for i in range(4):
	digits[i] = num % 256
	num //= 256

converted = 0
for item in digits:
	converted = converted * 256 + item

print (converted)