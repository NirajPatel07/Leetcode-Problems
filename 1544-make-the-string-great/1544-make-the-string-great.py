class Solution:
    def makeGood(self, s: str) -> str:
        # Initialise Stack
        stack = []
        
        for i in range(len(s)):
            # If element is present in stack and the condition is satfied 
            if stack and stack[-1] == s[i].swapcase():
                # then remove the top letter in stack
                stack.pop()
            else:
                # If the Condition is not satified then append the letter
                stack.append(s[i])
        
        # Return letter present in stack
        return ''.join(stack)