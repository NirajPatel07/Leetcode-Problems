class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = int((high-low)/2)
        
        if low%2!=0 or high%2!=0:
            count+=1
            
        return count