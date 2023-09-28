class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        end_point = len(nums) - 1
        
        for i in range(len(nums)):
            if i > max_jump:
                return False
            
            max_jump = max(max_jump, i + nums[i])
            
            if max_jump >= end_point:
                return True
        
        return False