class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(lambda: [])
        cnt = [-1 for _ in range(len(parent))]
        opt = 1

        for i in range(len(parent)):
            if s[i] == s[parent[i]]: parent[i] = -1
            children[parent[i]].append(i)

        def recursion(node):
            if cnt[node] != -1: return cnt[node]

            temp = [recursion(c) for c in children[node]]
            nonlocal opt

            if len(children[node]) == 0:
                cnt[node] = 1
            elif len(children[node]) == 1:
                cnt[node] = max([recursion(c) for c in children[node]]) + 1
                if cnt[node] > opt: opt = cnt[node]
            else:
                heap = [-recursion(c) for c in children[node]]
                heapify(heap)
                largest = -heappop(heap)
                largest2 = -heappop(heap)
                if largest + largest2 + 1 > opt: opt = largest + largest2 + 1
                cnt[node] = largest + 1

            return cnt[node]
        
        [recursion(c) for c in children[-1]]
            
        return opt