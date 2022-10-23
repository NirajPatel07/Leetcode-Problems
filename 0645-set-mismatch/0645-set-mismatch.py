class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        op = [0, 0]
        for i in range(1, len(nums)+1):
            if i in nums:
                if c[i] > 1:
                    op[0] = i
            else:
                op[1] = i
        
        return op
            