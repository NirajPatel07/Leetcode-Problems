class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for paren in s:
            if paren in "([{":
                stack.append(paren)
            else:
                if stack and stack[-1]==lookup[paren]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False