class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left, right, res, ind = 0, sum(nums), float('inf'), 0
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            left_eq = left // (i+1)
            right_eq = right // (len(nums) - i - 1) if right != 0 else 0
            temp = abs(left_eq - right_eq)
            if temp < res:
                ind, res = i, temp
        return ind