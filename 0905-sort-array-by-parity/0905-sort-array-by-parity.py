class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left < right:
            while left < len(nums) and nums[left] % 2 == 0:
                left += 1
            while right >= 0 and nums[right] % 2 == 1:
                right -= 1
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                
            left += 1
            right -= 1
        
        return nums
                