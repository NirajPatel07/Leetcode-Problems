class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        vowels_in_s = []
        for i, c in enumerate(s):
            if c in vowels:
                vowels_in_s.append(c)
                s[i] = None
        
        p = 0
        vowels_in_s = vowels_in_s[::-1]
        for i, c in enumerate(s):
            if c == None:
                s[i] = vowels_in_s[p]
                p+=1
        
        return ''.join(s)