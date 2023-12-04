class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        idx = 0
        
        for i in range(3, len(num) + 1):
            if len(set(num[idx:i])) == 1 and num[idx:i] > result:
                result = num[idx:i]    
            idx += 1
                
        return result