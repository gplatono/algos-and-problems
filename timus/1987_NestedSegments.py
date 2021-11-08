import sys

top = -1
seg_size = 0

def get_min(idx1, idx2):
	len1 = orig[idx1][1] - orig[idx1][0]
	len2 = orig[idx2][1] - orig[idx2][0]
	return idx1+1 if len1 < len2 else idx2+1
	
def search(target, arr):
	l = 0
	r = seg_size-1
	while l <= r:
		c = (l + r) >> 1
		if target >= arr[c][0] and target <= arr[c][1]:
			if target == arr[c][0] and c > 0 and target == arr[c-1][1]:				
				return get_min(arr[c][2], arr[c-1][2])
			elif target == arr[c][1] and c < seg_size - 1 and target == arr[c+1][0]:
				return get_min(arr[c][2], arr[c+1][2])				
			return arr[c][2] + 1
		elif target > arr[c][0]:
			if l < c:
				l = c
			else:
				l += 1
		else:
			if c < r:
				r = c
			else:
				r -= 1
	return -1

def add(segments, stack, seg):
	global top
	global seg_size
	while top > -1 and seg[0] > stack[top][1]:
		segments[seg_size] = stack[top]
		seg_size += 1
		top -= 1	
	if top == -1:
		stack[0] = seg
		top = 0
	else:
		left = [stack[top][0], seg[0], stack[top][2]] if stack[top][0] < seg[0] else None
		right = [seg[1], stack[top][1], stack[top][2]] if stack[top][1] > seg[1] else None
		if left is not None:			
			segments[seg_size] = left
			seg_size += 1
		if right is not None:
			stack[top] = right
		top += 1
		stack[top] = seg		
	#print (seg, segments, stack, top, seg_size)

n = int(input())
orig = [0]*n
segments = [0]*3*n
stack = [0]*(3*n)
for i in range(n):
	seg = [int(item) for item in input().split()] + [i]
	orig[i] = seg
	add(segments, stack, seg)
add(segments, stack, [1000000001, 1000000001, -1])

m = int(input())
for i in range(m):
	p = int(input())
	print(search(p, segments))