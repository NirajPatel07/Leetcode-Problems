class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        result = sum(nums[:3])
        nums.sort()
        
        for i in range(len(nums)):
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == target:
                    return curr_sum
                elif curr_sum > target:
                    right = right - 1
                else:
                    left = left + 1
                
                if abs(curr_sum-target) < abs(result-target):
                    result = curr_sum
        
        return result