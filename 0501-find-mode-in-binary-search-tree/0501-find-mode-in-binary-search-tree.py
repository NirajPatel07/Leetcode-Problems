# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        queue = [root]
        
        while queue:
            next_queue = []
            for root in queue:
                if root.val in count:
                    count[root.val] += 1
                else:
                    count[root.val] = 1
                    
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            
            queue = next_queue
        
        max_count = max(count.values())
        result = []
        
        for k, v in count.items():
            if v == max_count:
                result.append(k)
                
        return result