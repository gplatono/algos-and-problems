from typing import *


class Solution:
    def place_queens(self, col, n):
        """
        Fill in columns from 0 to n-1 by finding all the available rows
        for the current column
        """
        if col == n:
            return 1
        
        total_configs = 0
        for row in range(n):
            flag = False
            for i in range(col):
                #check if the queen in the (row, col) position would attack any previouly placed queen
                if row == self.pos[i] or row + col == i + self.pos[i] or row - col == self.pos[i] - i:
                    flag = True
                    break
                    
            #if the position (row, col) is good
            if not flag:
                self.pos[col] = row
                
                #If the entire board isn't filled yet, continue
                if col < n:
                    total_configs += self.place_queens(col+1, n)                   
                
        return total_configs
                    
    def totalNQueens(self, n: int) -> int:
        #List of row positions of queens, i.e., queens are at (pos[i], i)
        self.pos = [0] * n
        return self.place_queens(0, n)