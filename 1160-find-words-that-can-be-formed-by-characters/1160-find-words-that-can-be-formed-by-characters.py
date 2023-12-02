class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        result = 0
        
        for word in words:
            if not (Counter(word) - chars_count):
                result += len(word)
        
        return result