class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # create a dictionary to store subtrees
        subTrees = defaultdict(list)
        
        # define a DFS function to traverse the binary tree and find duplicate subtrees
        def dfs(node):
            # if the node is empty, return 'null'
            if not node:
                return 'null'
            
            # create a string representation of the current node and its subtrees
            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])
            
            # if the string representation is already in subTrees, then it's a duplicate subtree
            if len(subTrees[s]) == 1:
                # add the root node of one of the duplicate subtrees to the result list
                res.append(node)
                
            # add the current node to the list of nodes with the same string representation
            subTrees[s].append(node)
            
            # return the string representation of the current node and its subtrees
            return s
        
        # initialize an empty result list
        res = []
        
        # traverse the binary tree and find duplicate subtrees
        dfs(root)
        
        # return the root nodes of all the duplicate subtrees
        return res
