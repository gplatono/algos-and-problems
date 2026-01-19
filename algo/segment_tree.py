class SegmentTree:
    def __init__(self, data, merge_op, default):
        """Initialize the segment tree."""

        self.merge_op = merge_op
        self.default = default
        self.size = len(data)
        self.data = data
        self.tree = [default] * len(data) * 4
        self.build(1, 0, len(data) - 1)
    
    def build(self, idx, l, r):
        if l == r:
            self.tree[idx] = self.data[l]
        else:
            mid = (l + r) // 2
            self.build(2*idx, l, mid)
            self.build(2*idx + 1, mid + 1, r)
            self.tree[idx] = self.merge_op(self.tree[2*idx], self.tree[2*idx + 1])

    def query(self, idx, l, r, ql, qr):
        if l > qr or r < ql:            
            return self.default
        elif ql <= l <= r <= qr:
            return self.tree[idx]
        else:
            mid = (l + r) // 2
            return self.merge_op(self.query(2*idx, l, mid, ql, qr), self.query(2*idx+1, mid+1, r, ql, qr))
        
    def point_update(self, idx, l, r, pos, value):
        if l == r == pos:
            self.tree[idx] = value
        else:
            mid = (l + r) // 2
            if pos <= mid:
                self.point_update(2*idx, l, mid, pos, value)                
            else:                
                self.point_update(2*idx + 1, mid+1, r, pos, value)
            
            left_result = self.tree[2*idx]
            right_result = self.tree[2*idx+1]
            self.tree[idx] = self.merge_op(left_result, right_result)

tree = SegmentTree([1, 3, 5, 7, 9, 11], lambda x, y: x + y, 0)
print(tree.query(1, 0, tree.size - 1, 0, 5))  # Output: 36
tree.point_update(1, 0, tree.size - 1, 2, 10)
print(tree.query(1, 0, tree.size - 1, 2, 3))  # Output: 17
print(tree.query(1, 0, tree.size - 1, 0, 5))  # Output: 41