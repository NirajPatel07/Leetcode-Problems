class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d_w1 = Counter(word1)
        d_w2 = Counter(word2)

        return (sorted(d_w1.values()) == sorted(d_w2.values()) and
                sorted(d_w1.keys()) == sorted(d_w2.keys())
        )