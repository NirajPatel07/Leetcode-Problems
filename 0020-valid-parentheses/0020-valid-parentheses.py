class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for param in s:
            if param in "({[":
                stack.append(param)
            else:
                if stack and stack[-1] == lookup[param]:
                    stack.pop()
                else:
                    return False
        
        if stack: return False
        return True