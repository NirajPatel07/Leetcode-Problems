class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for j in range(len(nums)-1,-1,-1):
            for i in range(j):
                if str(nums[i])+str(nums[i+1])<str(nums[i+1])+str(nums[i]):
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    
        return str(int(''.join(map(str,nums))))