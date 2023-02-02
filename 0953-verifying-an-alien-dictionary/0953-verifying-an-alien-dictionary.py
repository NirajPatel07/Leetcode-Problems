class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Map each character to its index in the order
        order_index = {c: i for i, c in enumerate(order)}

        # Check each pair of adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Compare characters
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # If order is not sorted, return False
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            else:
                # If end of shorter word reached and length of first word is greater, return False
                if len(word1) > len(word2):
                    return False

        # If all pairs are sorted, return True
        return True


