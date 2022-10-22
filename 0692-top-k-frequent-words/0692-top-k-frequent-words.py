class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Sorting the List
        words = sorted(words)
        
        # Count the number of words using Counter
        c = Counter(words)
        
        # Return the k most common words
        return [word for word, _ in c.most_common(k)]