# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop(0)
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True