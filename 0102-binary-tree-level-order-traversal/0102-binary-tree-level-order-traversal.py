class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return None
        
        result = []
        queue = [root]
        next_queue = []
        curr_level = []
        
        while queue:
            for root in queue:
                curr_level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
                
            result.append(curr_level)
            curr_level = []
            queue = next_queue
            next_queue = []
        
        return result