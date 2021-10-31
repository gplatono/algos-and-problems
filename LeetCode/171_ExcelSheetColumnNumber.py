from typing import Any

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        power = 1
        for i in range(len(columnTitle)-1, -1, -1):
            number += (ord(columnTitle[i])-64) * power
            power *= 26
        
        return number