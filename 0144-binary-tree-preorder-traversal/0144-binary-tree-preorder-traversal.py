# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return root
        
        def preorder(root, res):
            res.append(root.val)
            
            if root.left:
                preorder(root.left, res)
            
            if root.right:
                preorder(root.right, res)
                
        res = []
        preorder(root, res)
        
        return res