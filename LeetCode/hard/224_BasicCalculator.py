from typing import *

class Solution:
    def processNum(self, num: int, stack: List[object]):
        if stack == [] or stack[-1] == '(':
            stack.append(num)
        else:
            op = stack.pop(-1)
            if op == '+':
                stack[-1] = stack[-1] + num
            elif op == '-':
                if stack != [] and stack[-1] != '(':
                    stack[-1] = stack[-1] - num
                elif stack == [] or stack[-1] == '(':
                    stack.append(-num)

    def calculate(self, s: str) -> int:
        stack = []
        numline = ""
        for i in s:
            if i >= '0' and i <= '9':
                numline += i
            else:
                if numline != "":
                    self.processNum(int(numline), stack)                    
                    numline = ""
                if i == '+' or i == '-' or  i == '(':
                    stack.append(i)
                elif i == ')':
                    num = stack.pop(-1)
                    stack.pop(-1)
                    self.processNum(num, stack)                    
    
        if numline != "":
            self.processNum(int(numline), stack)
        
        return stack[-1]
        