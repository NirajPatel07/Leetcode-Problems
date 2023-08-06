class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # initialize the count and candidate variables
        count = 0
        candidate = None
        
        # iterate through the array
        for num in nums:
            # if count is 0, update the candidate variable
            if count == 0:
                candidate = num
            # increment or decrement count based on whether the current element is the candidate
            count += (1 if num == candidate else -1)
        
        # return the candidate variable
        return candidate