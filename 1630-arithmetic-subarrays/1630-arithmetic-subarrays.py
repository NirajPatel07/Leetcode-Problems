from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(subarray):
            n = len(subarray)
            if len(subarray) <= 2:
                return True

            min_val, max_val = min(subarray), max(subarray)

            if (max_val - min_val) % (n - 1) != 0:
                return False

            common_diff = (max_val - min_val) // (n - 1)
            seen = set(subarray)

            if common_diff == 0:
                return len(seen) == 1

            for i in range(min_val, max_val + 1, common_diff):
                if i not in seen:
                    return False

            return True

        ans = []
        for x, y in zip(l, r):
            ans.append(is_arithmetic(nums[x: y + 1]))

        return ans
