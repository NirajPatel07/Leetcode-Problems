class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        last_moment = 0
        
        for l in left:
            last_moment = max(l, last_moment)
            
        for r in right:
            last_moment = max(last_moment, n-r)
        
        return last_moment