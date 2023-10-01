class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        result = []
        
        for word in word_list:
            result.append(word[::-1])
        
        return ' '.join(result)