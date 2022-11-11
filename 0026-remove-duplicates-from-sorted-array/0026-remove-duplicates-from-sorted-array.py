class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        
        while right<len(nums):
            while right<len(nums) and nums[left] == nums[right]:
                right+=1
            if right<len(nums):
                nums[left+1], nums[right] = nums[right], nums[left+1]
                left+=1
                right+=1
            else:
                break
        
        return left+1
            