class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = []
        for d, s in zip(dist, speed):
            minReach.append(math.ceil(d/s))
            
        minReach.sort()
        res = 0
        for minute in range(len(minReach)):
            if minute >= minReach[minute]:
                return res
            res += 1
        
        return res