# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            queue = [root]
            total, node_count = 0, 0
            
            while queue:
                next_queue = []
                for root in queue:
                    total += root.val
                    node_count += 1
                    
                    if root.left:
                        next_queue.append(root.left)
                    if root.right:
                        next_queue.append(root.right)
                queue = next_queue
            
            return (total, node_count)
        
        def check(root):
            if not root:
                return
            
            subtree_sum, node_count = bfs(root)
            average = 0
            if subtree_sum != 0:
                average = subtree_sum // node_count
            
            if root.val == average:
                self.result += 1
            
            if root.left:
                check(root.left)
            if root.right:
                check(root.right)
            
        
        self.result = 0
        check(root)
        return self.result
            
            