class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        print('i', i)
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        print('i', i)
        
        # if i < 0:
        #     nums.reverse()
        
        if i >= 0:
            j = len(nums) - 1
            print('j', j)
            while j > i and nums[j] <= nums[i]:
                j -= 1
            print('j', j)
            nums[i], nums[j] = nums[j], nums[i]
        
        print(nums)
        nums[i+1:] = reversed(nums[i+1:])
        
        return nums
            