class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        large1 = 0
        large2 = 0
        small1 = float("inf")
        small2 = float("inf")
        for i in nums:
            if i>large1:
                large2 = large1
                large1 = i
            elif i>large2:
                large2 = i
            if i<small1:
                small2 = small1
                small1 = i
            elif i<small2:
                small2 = i
        return (large1*large2) - (small1*small2)