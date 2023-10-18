class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        relate = defaultdict(list)
        for a,b in relations:
            relate[b].append(a)


        values = [0]*n
        def dp(node):
            if(values[node-1] > 0):
                return values[node-1]
            cur = time[node-1]
            #the time it takes to run current node
            #is the max time of the previous nodes plus current time
            a = [0]
            for i in relate[node]:
                a.append(dp(i))
            values[node-1] = max(a) + cur
            return values[node-1]
        
        a = 0
        for i in range(1,n+1):
            a = max(dp(i),a)
            
        return a