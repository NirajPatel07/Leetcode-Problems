class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count, left = 0, 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                count += right
                left = right

        return count