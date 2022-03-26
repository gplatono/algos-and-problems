from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        pows = [1]
        y = x if n > 0 else 1/x
        while y <= 10000 and y >= -10000 and len(pows) <= 34:
            pows.append(y)
            y *= y
            
        m = n if n >= 0 else -n        
        pow2 = 32
        res = 1
        while pow2 >= 0:
            if m // (2 ** pow2) >= 1:                
                res *= pows[pow2 + 1]
                m = m % (2 ** pow2)
            pow2 -= 1
        
        return res