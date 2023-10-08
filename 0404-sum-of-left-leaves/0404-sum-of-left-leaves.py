# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, left):
            if not root:
                return
            
            if left and not root.left and not root.right:
                left_leaf.append(root.val)
            
            dfs(root.left, True)
            dfs(root.right, False)
        
        left_leaf = []
        dfs(root, False)
        return sum(left_leaf)
            