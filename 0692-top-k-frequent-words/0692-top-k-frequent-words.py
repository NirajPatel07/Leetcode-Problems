class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        counts = Counter(words)
        return [word for word, _ in counts.most_common(k)]