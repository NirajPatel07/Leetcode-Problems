# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        def postorder(root, res):
            if root.left:
                postorder(root.left, res)
            
            if root.right:
                postorder(root.right, res)
                
            res.append(root.val)
        
        res = []
        postorder(root, res)
        
        return res
            