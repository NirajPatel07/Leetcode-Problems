class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = collections.defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        res = [0] * n
        visited = set()
        def dfs(node):
            # When a recursive call is complete, we need to return 
            # the number of each labels we saw.
            # update the resulting list
            if node is None:
                return collections.defaultdict(int)
            visited.add(node)
            subtree = collections.defaultdict(int)
            subtree[labels[node]] += 1

            for adj_node in adj_list[node]:
                if adj_node not in visited:
                    adj_tree = dfs(adj_node)

                    for k, v in adj_tree.items():
                        subtree[k] += v
            res[node] = subtree[labels[node]]
            return subtree
        dfs(0)
        return res