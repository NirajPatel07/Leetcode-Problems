class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        while 0 in nums:
            nums.remove(0)
            c += 1
            
        while c > 0:
            nums.append(0)
            c -= 1
        
        return nums
        
        