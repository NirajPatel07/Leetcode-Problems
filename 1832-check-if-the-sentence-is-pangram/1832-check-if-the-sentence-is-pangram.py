class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = Counter(sentence)
        if len(c) == 26:
            return True
        return False