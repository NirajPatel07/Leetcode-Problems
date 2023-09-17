class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:

                mid_left, mid_right = mid, mid
                
                while mid_left-1 >= 0 and nums[mid_left-1] == nums[mid]:
                    mid_left -= 1
                while (mid_right+1) <= (len(nums)-1) and nums[mid_right+1] == nums[mid]:
                    mid_right += 1
                
                return [mid_left, mid_right]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [-1, -1]
                    
                