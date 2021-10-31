from typing import Any

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        
        while columnNumber > 0:           
            digit = columnNumber % 26
            if digit == 0:
                digit = 26
                columnNumber -= 26
                
            columnNumber //= 26                
            s = chr(digit + 64) + s
            
        return s