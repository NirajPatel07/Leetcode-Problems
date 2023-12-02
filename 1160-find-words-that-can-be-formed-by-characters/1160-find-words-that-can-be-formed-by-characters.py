class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        result = 0
        
        for word in words:
            word_count = {}
            word_length = len(word)
            for i, c in enumerate(word):
                if c in word_count:
                    word_count[c] += 1
                else:
                    word_count[c] = 1
                
                if c not in char_count or word_count[c] > char_count[c]:
                    break
                
                if i == word_length - 1:
                    result += word_length
        
        return result
                    
                
            