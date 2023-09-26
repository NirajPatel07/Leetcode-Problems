class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        seen = set()
        stack = []
        
        for c in s:
            if c in seen:
                count[c] -= 1
            else:
                while stack and stack[-1] > c and count[stack[-1]] > 0:
                    seen.remove(stack[-1])
                    stack.pop()
                    
                seen.add(c)
                stack.append(c)
                count[c] -= 1
                
        return ''.join(stack)
        