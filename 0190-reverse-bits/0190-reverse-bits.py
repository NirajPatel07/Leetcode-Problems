class Solution:
    def reverseBits(self, n: int) -> int:
        s=bin(n)
        s=s[2:]
        s=s[::-1] + ("0"*(32-len(s)))
        return int(s,2)