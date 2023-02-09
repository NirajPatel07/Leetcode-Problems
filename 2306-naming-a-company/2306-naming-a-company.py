from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Create 26 empty sets to store words starting with each letter
        groups = [set() for i in range(26)]
        for idea in ideas:
            # Add each word to its respective set based on its first letter
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        answer = 0
        # Iterate through all 26 sets
        for i in range(25):
            for j in range(i+1, 26):
                # Calculate the number of mutual ideas (ideas with same suffix)
                mutuals = len(groups[i] & groups[j])
                # For each group, the number of unique combinations of two words from different groups is
                # equal to the product of the number of words in each group minus the number of mutual words
                answer += 2 * (len(groups[i]) - mutuals) * (len(groups[j]) - mutuals)
        
        return answer
