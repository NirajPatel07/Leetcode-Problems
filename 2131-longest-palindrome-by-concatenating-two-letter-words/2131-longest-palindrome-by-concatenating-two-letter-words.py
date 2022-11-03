class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        lookup = Counter(words)
        p_len = 0
        mid = 0
        
        for word in lookup.keys():
            if word[0] == word[1]:
                if lookup[word]%2 == 0:
                    p_len += lookup[word]
                else:
                    p_len += lookup[word]-1
                    mid = 1
                    
            elif word[::-1] in lookup:
                p_len += min(lookup[word], lookup[word[::-1]])
        
        return (p_len + mid) * 2