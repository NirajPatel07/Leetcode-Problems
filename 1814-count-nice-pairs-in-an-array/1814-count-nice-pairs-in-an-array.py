class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = {}
        mod = 10 ** 9 + 7
        count = 0
        
        for i in range(len(nums)):
            # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
            # Is same as
            # nums[i] - rev(nums[i]) == nums[j] -  rev(nums[j])
            curr = nums[i] - self.reverse(nums[i])
            counter[curr] = counter.get(curr, 0) + 1
        
        for n in counter:
            count += (counter[n] * (counter[n] - 1)) // 2
        
        return count % mod
            
    def reverse(self, x):
        reversed_num = 0
        
        while x > 0:
            remainder = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + remainder
            
        return reversed_num
            