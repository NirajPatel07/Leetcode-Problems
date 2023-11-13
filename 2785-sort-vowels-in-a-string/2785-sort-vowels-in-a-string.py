class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        
        s_vowels = []
        for c in s:
            if c not in vowels:
                continue
            s_vowels.append(c)
            
        s_vowels.sort()
        result = ""
        
        idx = 0
        for c in s:
            if c not in vowels:
                result += c
            else:
                result += s_vowels[idx]
                idx += 1
                
        if idx < len(s_vowels):
            while idx < len(s_vowels):
                result += s_vowels[idx]
                idx += 1
                
        return result
        
        
                
        