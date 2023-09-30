class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # [n, min_left]
        curr_min = nums[0]
        
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
                
            if stack and n > stack[-1][1]:
                return True
            
            stack.append([n, curr_min])
            curr_min = min(n, curr_min)
        
        return False