

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.bal = 0

    def insert(self, node, par_bal=None):
        if self.value <= node.value:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(node)
            self.bal -= 1
        else:
            if self.left == None:
                self.left = node
            else:
                self.left.insert(node)
            self.bal += 1
        
        if self.bal = 2