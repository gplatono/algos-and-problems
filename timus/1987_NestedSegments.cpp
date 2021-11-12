#import <iostream>
using namespace std;

struct point
{
    int x;
    int y;
    int i;

    Point(int x, int y, int i)
    {
        this.x = x;
        this.y = y;
        this.i = i;
    }
}

int top = -1;
int seg_size = 0;
int segments[300000][3];
int stack[300000][3];
int orig[100001][2];

int get_min(int idx1, int idx2)
{
	int len1 = orig[idx1][1] - orig[idx1][0];
	int len2 = orig[idx2][1] - orig[idx2][0];
    if (len1 < len2)
        return idx1 + 1;
    else
        return idx2 + 1;
}
	
int search(target)
{
	int l = 0;
	int r = segsize-1;
	while (l <= r)
    {
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
    }
	return -1;
}

void add(int idx)
{
	while (top > -1 && orig[idx][0] > stack[top][1])
    {
		segments[seg_size][0] = stack[top][0];
        segments[seg_size][1] = stack[top][1];
        segments[seg_size][2] = stack[top][2];
		seg_size += 1
		top -= 1	
    }
	if (top == -1)
    {
		stack[0][0] = orig[idx][0];
        stack[0][1] = orig[idx][1];
        stack[0][2] = idx;
		top = 0;
    }
	else:
        Point left = NULL;
        if (stack[top].x < seg.x)
            left = {stack[top].x, seg.x, stack[top].i};
        Point right = NULL;
        if (stack[top].y > seg.y)
            right = {seg.y, stack[top].y, stack[top].i);
		if left != NULL:			
			segments[seg_size] = left
			seg_size += 1
		if right != NULL:
			stack[top] = right
		top += 1
		stack[top] = seg		
	#print (seg, segments, stack, top, seg_size)
}

int main(int argc, char** argv) 
{
    int n, m;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int l, r;
        cin >> orig[i][0] >> orig[i][1];
        add(index);
    }
    orig[n][0] = 1000000001;
    orig[n][1] = 1000000001;
    add(n);

    cin >> m;
    for (int i = 0; i < m; i++)
    {   
        int p;
        cin >> p;
        cout << search(p);
    }
    return 0;
}