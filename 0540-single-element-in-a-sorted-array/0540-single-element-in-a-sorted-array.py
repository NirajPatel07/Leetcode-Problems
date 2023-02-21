class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        for n in c:
            if c[n] == 1:
                return n