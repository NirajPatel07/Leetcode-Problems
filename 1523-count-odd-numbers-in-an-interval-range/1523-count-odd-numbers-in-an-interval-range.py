class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Initialize count to the number of even integers between low and high
        count = int((high-low)/2)
        
        # Check if either low or high is odd. 
        # If either is odd, we add 1 to the count to account for the extra odd integer
        if low%2!=0 or high%2!=0:
            count+=1
            
        # Return the final count
        return count
