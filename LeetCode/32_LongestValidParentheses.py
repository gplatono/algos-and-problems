from typing import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        running = 0
        maxx = 0
        for c in s:
            #print (c, running, maxx, stack)
            if c == ')':
                if len(stack) > 0 and stack[-1] != ')':
                    if stack[-1] == '(':
                        running += 2
                        stack.pop(-1)
                        while len(stack) > 0 and stack[-1] != ')' and stack[-1] != '(':
                            running += stack[-1]
                            stack.pop(-1)
                        maxx = max(maxx, running)                            
                else:
                    stack.append(running)
                    stack.append(c)
                    running = 0
            elif c == '(':
                if running > 0:
                    stack.append(running)
                    running = 0
                stack.append(c)
                
        return maxx