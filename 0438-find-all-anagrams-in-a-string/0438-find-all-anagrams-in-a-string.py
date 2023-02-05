class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        
        n = len(p)
        c1 = Counter(p)
        op = []
        for i in range(len(s)-n+1):
            #print(s2[i:i+n])
            if Counter(s[i:i+n]) == c1:
                op.append(i)
            
        return op