class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        lookup = {}
        res = 1
        
        for word in words:
            lookup[word] = 1
            for i in range(len(word)):
                successor = word[:i] + word[i+1:]
                if successor in lookup:
                    lookup[word] = max(lookup[word], 1 + lookup[successor])
                    
        res = max(lookup.values())
        return res