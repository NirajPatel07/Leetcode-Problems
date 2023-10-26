class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [2, 1, 9, 11, 1]
        # [2, 1, 11, 13, 12]
        
        # [2,7,9,3,1]
        # [2, 7, 11, 10, 12]
        
        # [1,2,3,1]
        # [1, 2, 4, 3]
        
        if len(nums) < 3:
            return max(nums)
        
        dp = []
        dp.append(nums[0])
        dp.append(nums[1])
        
        for i in range(2, len(nums)):
            curr1, curr2 = 0, 0
            if i-2 >= 0:
                curr1 = dp[i-2] + nums[i]
            if i-3 >= 0:
                curr2 = dp[i-3] + nums[i]
            curr_max = max(curr1, curr2)
            dp.append(curr_max)
        
        print(dp)
        return max(dp[len(nums)-1], dp[len(nums)-2])