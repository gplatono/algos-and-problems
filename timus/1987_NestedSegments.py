import sys

def binarySearch(target, arr):
	l = 0
	r = len(arr)
	while (l <= r):
		c = (l + r) >> 1
		if target < arr[c][0]:
			r = c
		elif target > arr[c][1]:
			l = c

n = int(input())
segments = []
for i in range(n):	
	segments.append([int(item) for item in input().split()])
m = int(input())
for i in range(m):
	p = int(input())

print(segments)