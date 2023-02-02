class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary mapping each character in the order to its index
        order_index = {c: i for i, c in enumerate(order)}

        # Iterate over each pair of adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Compare characters in the words
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # If the characters are different and their order is not sorted, return False
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            else:
                # If the end of the shorter word is reached and the length of the first word is greater, return False
                if len(word1) > len(word2):
                    return False

        # If all pairs of words are sorted, return True
        return True


