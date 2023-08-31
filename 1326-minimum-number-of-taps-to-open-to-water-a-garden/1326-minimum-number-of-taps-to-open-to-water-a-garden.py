class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n+1)
        
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            
            max_reach[left] = max(max_reach[left], right)
            
        
        end, far_can_reach, tap_used = 0, 0, 0
        
        for i, reach in enumerate(max_reach):
            if i > end:
                if far_can_reach <= end:
                    return -1
                
                end = far_can_reach
                tap_used += 1
            
            far_can_reach = max(far_can_reach, reach)
            
        return tap_used + (end < n)
        