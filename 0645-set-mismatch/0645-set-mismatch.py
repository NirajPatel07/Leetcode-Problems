class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        total_sum = sum(nums)
        set_sum = sum(set(nums))
        total_n_sum = length*(length+1)//2
        
        return [total_sum - set_sum, total_n_sum - set_sum]