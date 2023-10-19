class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace_string(s):
            stack = []
            
            for i in range(len(s)):
                if s[i] == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(s[i])
            
            return "".join(stack)
        
        str1 = backspace_string(s)
        str2 = backspace_string(t)
        
        return str1 == str2