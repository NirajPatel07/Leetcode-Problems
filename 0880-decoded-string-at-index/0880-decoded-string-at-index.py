class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        
        for d in s:
            if d.isdigit():
                size = size * int(d)
            else:
                size += 1
                
        for c in reversed(s):
            k = k % size
            if (k == 0 or k == size) and c.isalpha():
                return c
            if c.isdigit():
                size = size // int(c)
            else:
                size -= 1