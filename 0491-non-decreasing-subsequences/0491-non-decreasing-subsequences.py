class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        LIS = [[[num]] for num in nums]
        for i in range(length):
            for j in range(i+1, length):
                if nums[j]>= nums[i]:
                    LIS[j]+=[item + [nums[j]] for item in LIS[i]]
                    
        # print(LIS)
        res = []
        seen = set()
        for sublist in LIS:
            for ele in sublist:
                if tuple(ele) not in seen and len(ele)>1:
                    seen.add(tuple(ele))
                    res.append(ele)
        return res