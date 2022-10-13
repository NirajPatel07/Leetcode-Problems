"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        output = []
        
        while stack:
            top = stack.pop()
            output.append(top.val)
            stack.extend(reversed(top.children))
        
        return output