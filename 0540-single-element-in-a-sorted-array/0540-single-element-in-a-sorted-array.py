class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # if the adjacent elements are equal to the midpoint element,
            # then the single element is on the right side of the array
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            # otherwise, the single element is on the left side of the array
            else:
                right = mid
        
        # return the value at the left index, which is the index of the single element in the array
        return nums[left]
