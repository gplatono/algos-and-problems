#import <iostream>
using namespace std;

struct Point
{
    int x;
    int y;
    int i;

    void prinT()
    {
        cout << "[" << x << ", " << y << ", " << i << "]" << endl;
    }
};

int top = -1;
int seg_size = 0;
Point segments[300000];
Point stack[300000];
Point orig[100001];

void printall()
{
    cout << "STACK START: " << endl;
    for (int i = 0; i <= top; i++)
        stack[i].prinT();
    cout << "STACK END" << endl;
    for (int i = 0; i <seg_size; i++)
         segments[i].prinT();  
    cout << "SEG END " << endl;
	cout << top << " " << seg_size << endl;
}

int get_min(int idx1, int idx2)
{
	int len1 = orig[idx1].y - orig[idx1].x;
	int len2 = orig[idx2].y - orig[idx2].x;
    if (len1 < len2)
        return idx1 + 1;
    else
        return idx2 + 1;
}
	
int srch(int target)
{
	int l = 0;
	int r = seg_size-1;
	while (l <= r)
    {
		int c = (l + r) >> 1;
		if (target >= segments[c].x && target <= segments[c].y)
        {
			if (target == segments[c].x && c > 0 && target == segments[c-1].y)
				return get_min(segments[c].i, segments[c-1].i);
			else if (target == segments[c].y && c < seg_size - 1 && target == segments[c+1].x)
				return get_min(segments[c].i, segments[c+1].i);				
			return segments[c].i + 1;
        }
		else if (target > segments[c].x)
        {
			if (l < c)
				l = c;
			else
				l += 1;
        }
		else
        {
			if (c < r)
				r = c;
			else
				r -= 1;
        }
    }
	return -1;
}

void add(int idx)
{    
    while (top > -1 && orig[idx].x > stack[top].y)
    {
		segments[seg_size] = stack[top];
		seg_size += 1;
		top -= 1;
    }
	if (top == -1)
    {
		stack[0] = orig[idx];
		top = 0;
    }
	else
    {
        Point left = {-1, -1, -1}, right = {-1, -1, -1};
        if (stack[top].x < orig[idx].x)
            left = {stack[top].x, orig[idx].x, stack[top].i};
        if (stack[top].y > orig[idx].y)
            right = {orig[idx].y, stack[top].y, stack[top].i};
        
		if (left.x != -1) 
        {
			segments[seg_size] = left;
			seg_size += 1;
        }
		if (right.x != -1)
        {
			stack[top] = right;
            top += 1;
        }
		stack[top] = orig[idx];
    }
    //printall();
}

int main(int argc, char** argv)
{
    int n, m;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int l, r;
        cin >> l >> r;
        orig[i] = {l, r, i};
        add(i);
    }
    orig[n] = {1000000001, 1000000001, n};
    add(n);

    cin >> m;
    for (int i = 0; i < m; i++)
    {   
        int p;
        cin >> p;
        cout << srch(p) << endl;
    }
    return 0;
}