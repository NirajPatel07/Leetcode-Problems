class Solution:
    def jump(self, nums):
        # Initialize the number of steps required to reach the last index
        steps = 0
        
        n = len(nums)
        
        # currEnd keeps track of the end of the current step
        currEnd = 0
        
        # currFarthest keeps track of the farthest point that can be reached in the current step
        currFarthest = 0
        
        # Iterate through the nums array
        for i in range(n-1):
            # Update the farthest point that can be reached
            currFarthest = max(currFarthest, i + nums[i]) 
            
            # If we have reached the end of the current step, increment the number of steps
            if i == currEnd: 
                steps += 1
                # Update the end of the current step to the farthest point
                currEnd = currFarthest 
        
        # Return the number of steps   
        return steps 
