class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_strings = ['000','111','222','333','444','555','666','777','888','999']
        max_value = []
        
        for n in good_strings:
            if n in num:
                max_value.append(n)
                
        max_value.sort()
        
        return max_value[-1] if max_value else ""