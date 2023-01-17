class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        # Mapping of which nodes are connected.
        # First everyone is just connected to itself.
        p = list(range(n))
        # Number of values in a subgraph.
        # Initially each node is a subgraph with just one value.
        count = [Counter({vals[i]:1}) for i in range(n)]
        # We need to start with smallest value which has little to no connection.
        # Later, larger subgraphs will be build by connecting bigger values.
        edges = sorted((max(vals[i],vals[j]),i,j) for i,j in edges)
        # Each node is connected to itself and counts as a path.
        res = n

        def find(i):
            """Union find implementation.
            
            We just add, which node a future occuring node is connected to, 
            to find the root.
            """
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        # Iterate from smallest to largest value
        for val, i, j in edges:
            # Determine the root nodes/subtrees.
            # Note, originally, there is no connection.
            pi, pj = find(i), find(j)
            # If both subtress have the currently observed value,
            # we found a valid path.
            # Count will return 0 in most cases,
            # because values in subtrees are different.
            # Each value in one subtree now has
            # exact one path to each value in the other subtree.
            res += count[pi][val] * count[pj][val]
            # Join the subtrees.
            # If pi=pj, nothing would change.
            # Otherwise, find(i) will now return pj, which is also find(j).
            p[pi] = pj
            # Smaller values were counted already.
            # If pi and pj, had the same current max value,
            # we now have to combine it for future counts.
            # Note that higher values will be considered later,
            # once the respective edges pop up.
            count[pj][val] += count[pi][val]
        return res