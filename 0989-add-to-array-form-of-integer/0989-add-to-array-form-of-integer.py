class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = ''
        for i in num:
            n+=str(i)
        total = int(n)+k
        
        res = [int(n) for n in str(total)]
        return res