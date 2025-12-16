# Misra-Gries Summary and Heavy Hitters algorithm for finding 
# k-reduced bag for and most frequent items in a stream or an array.
class MisraGries():
    def __init__(self, k: int, use_fast_implementation=True):
        self.k = k
        self.use_fast = use_fast_implementation
        self.k_bag = [(None, 0)] * (k-1)
        self.fast_k_bag = {}

    def ingest(self, a: int):
        if self.use_fast:
            self.fast_ingest(a)
        else:
            self.slow_ingest(a)
    
    # O(k) k-bag processing
    def slow_ingest(self, a: int):
        first_empty = -1
        for i in range(len(self.k_bag)):
            if self.k_bag[i][0] == None and first_empty == -1:
                first_empty = i
            if a == self.k_bag[i][0]:
                self.k_bag[i] = (a, self.k_bag[i][1] + 1)
                return        
        
        if first_empty != -1:
            self.k_bag[first_empty] = (a, 1)
        else:
            for i in range(len(self.k_bag)):
                if self.k_bag[i][1] > 1:
                    self.k_bag[i] = (a, self.k_bag[i][1] - 1)
                else:
                    self.k_bag[i] = (None, 0)

    # O(log k) k-bag processing
    def fast_ingest(self, a: int):
        if a in self.fast_k_bag:
            self.fast_k_bag[a] += 1
        else:
            if len(self.fast_k_bag.keys()) < self.k - 1:
                self.fast_k_bag[a] = 1
            else:
                new_bag = {}
                for k in self.fast_k_bag.keys():
                    if self.fast_k_bag[k] > 1:
                        new_bag[k]  = self.fast_k_bag[k] - 1
                self.fast_k_bag = new_bag

    def retrieve_summary(self):
        if self.use_fast:
            return [key for key in self.fast_k_bag.keys()]
        else:
            return [item[0] for item in self.k_bag if item[0] != None]

mg = MisraGries(3, True)
#[mg.ingest(item)for item in [1, 2, 1, 2, 3, 3, 1, 2, 3, 4]]
[mg.ingest(item)for item in [3, 2, 3, 4, 5]]

print(mg.retrieve_heavy_hitters())