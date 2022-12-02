class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_w1 = Counter(word1)
        count_w2 = Counter(word2)
        
        keys_compare = sorted(count_w1.keys()) == sorted(count_w2.keys())
        vaules_compare = sorted(count_w1.values()) == sorted(count_w2.values())
                                                             
        return keys_compare and vaules_compare