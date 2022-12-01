class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        '''
        n = len(s)
        mid = n//2
        a = s[:mid]
        b = s[mid:]
        
        a_count = Counter(a)
        b_count = Counter(b)
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a_vowel = 0
        for c in a_count:
            if c in vowels:
                a_vowel+=a_count[c]
        
        b_vowel = 0
        for c in b_count:
            if c in vowels:
                b_vowel+=b_count[c]
                
        return a_vowel == b_vowel '''
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        right = len(s)-1
        left = 0
        a_vowel = 0
        b_vowel = 0
        
        while left<right:
            if s[left] in vowels:
                a_vowel+=1
            if s[right] in vowels:
                b_vowel+=1
            left+=1
            right-=1
        
        return a_vowel == b_vowel
        