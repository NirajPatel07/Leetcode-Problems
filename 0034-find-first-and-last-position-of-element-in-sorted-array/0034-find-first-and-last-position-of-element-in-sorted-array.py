class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = right = mid
                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                while right + 1 < len(nums) and nums[right + 1] == target:
                    right += 1
                return [left, right]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [-1, -1]