class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for s in columnTitle:
            n=(ord(s)-ord('A'))+1
            res=res*26+n
        return res