# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def bfs(root):
            
            queue = [root]
            while queue:
                curr_queue = []
                root_values = []
                
                for root in queue:
                    root_values.append(root.val)
                    if root.left:
                        curr_queue.append(root.left)
                    if root.right:
                        curr_queue.append(root.right)
                        
                result.append(max(root_values))
                queue = curr_queue
        
        result = []
        bfs(root)
        return result