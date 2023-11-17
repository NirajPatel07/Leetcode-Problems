class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        
        for i in range(len(nums)//2):
            pairs.append(nums[i] + nums[~i])
            
        return max(pairs)
        