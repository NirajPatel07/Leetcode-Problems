class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        stackVowel = []
        stackIndex = []
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        for i in range(len(s)):
            if s[i] in vowels:
                stackVowel.append(s[i])
                stackIndex.append(i)
        
        stackVowel.sort()

        for i in range(len(stackVowel)):
            s[stackIndex[i]] = stackVowel[i]
        return "".join(s)