from typing import *


class Solution:    
    def place_queens(self, col, n):
        """
        Fill in columns from 0 to n-1 by finding all the available rows
        for the current column
        """
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
                if col < n-1:
                    self.place_queens(col+1, n)

                #Fill-in and save the board configuration based on selected row-col pairs
                else:                   
                    board = [""] * n
                    for i in range(n):
                        for j in range(n):
                            board[i] += 'Q' if self.pos[i] == j else '.'
                            
                    self.boards.append(board)
        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        #List of row positions of queens, i.e., queens are at (pos[i], i)
        self.pos = [0] * n
        self.boards = []        
        self.place_queens(0, n)

        return self.boards