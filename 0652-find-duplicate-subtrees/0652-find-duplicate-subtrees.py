class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTrees = defaultdict(list)
        
        def dfs(node):
            if not node:
                return 'null'
            
            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subTrees[s]) == 1:
                res.append(node)
            subTrees[s].append(node)
            return s
        
        res = []
        dfs(root)
        return res
        