class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # create an empty list to store the shuffled elements
        res = [] 
        
        # loop through the first half of the elements (n elements)
        for i in range(n): 
            # add the current element and the corresponding element from the 
            # second half of the elements to the result list
            res.extend([nums[i], nums[i+n]])
        
        # return the shuffled list
        return res