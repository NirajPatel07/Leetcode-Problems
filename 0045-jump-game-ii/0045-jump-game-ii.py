class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # jumps[i] stores the minimum number of jumps to reach index i
        jumps = [0] * n
        
        for i in range(1, n):
            
            jumps[i] = float('inf')
            
            for j in range(i):
                
                # check if index i can be reached from index j
                if i <= j + nums[j] and jumps[j] != float('inf'):
                    
                    # update the minimum number of jumps to reach index i
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
                    
        # return the minimum number of jumps to reach the last index
        return jumps[-1]
