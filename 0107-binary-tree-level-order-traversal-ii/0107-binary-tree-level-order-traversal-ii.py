# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = [root]
        result = []
        
        while queue:
            curr_queue = []
            curr_level = []
            
            while queue:
                root = queue.pop(0)
                curr_level.append(root.val)
                if root.left:
                    curr_queue.append(root.left)
                if root.right:
                    curr_queue.append(root.right)
                    
            queue = curr_queue
            result.append(curr_level)
            
        return result[::-1]