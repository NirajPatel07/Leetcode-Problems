class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        res = ""
        keys = list(mapping.keys())
        keys.sort(reverse=True)
        
        for n in keys:
            while n <= num:
                res += mapping[n]
                num = num - n
                # print(num)
                
        return res
            
            
        
        