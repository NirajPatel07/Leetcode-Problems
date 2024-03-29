class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0
        
        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1
            
            count = j - i
            ans = min(ans, n - count)

        return ans