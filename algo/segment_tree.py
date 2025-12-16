class SegmentTree:
    def __init__(self, func, default):
        """Initialize the segment tree."""

        self.func = func
        self.default = default
        self.size = 0
    
    def build(self, data):
        
