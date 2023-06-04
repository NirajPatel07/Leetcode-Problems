class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in digits:
            num = num * 10 + n
        
        num = num+1
        res = []
        
        while num>0:
            res.insert(0, num%10)
            num = num // 10
        
        return res
        