class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for parentheses in s:
            if parentheses in "([{":
                stack.append(parentheses)
            else:
                if stack and lookup[parentheses] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False