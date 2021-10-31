import math
from typing import Any

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n+1)]
        res = ""
        
        while n > 0:       
            fact = math.factorial(n-1)
            ind = (k-1) // fact
            k %= fact
            n -= 1
            res += digits[ind]
            digits.pop(ind)
            
        return res