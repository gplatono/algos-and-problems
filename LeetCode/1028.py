from typing import Any

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def attach(self, stack, depth, num):
        while len(stack) > depth:
            stack.pop(-1)
        node = TreeNode(val=num)
        if len(stack) > 0:
            if stack[-1].left is None:
                stack[-1].left = node
            else:
                stack[-1].right = node
        stack.append(node)
        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        num = 0
        depth = 0
        for c in traversal:
            if c >= '0' and c <= '9':
                num = num*10 + int(c)                
            else:
                if num != 0:
                    self.attach(stack, depth, num)
                    num = 0
                    depth = 0
                depth += 1
                
        if num != 0:
            self.attach(stack, depth, num)
                
        return stack[0]