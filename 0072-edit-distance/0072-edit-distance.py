class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of the input strings
        len1, len2 = len(word1), len(word2)
        # Initialize a 2D list to store the minimum edit distances
        # between prefixes of the input strings
        # dp[i][j] represents the minimum number of edits required to convert
        # the first i characters of word1 to the first j characters of word2
        dp = [[-1] * (len2+1) for _ in range(len1+1)]
        
        # Fill in the first row and column of the dp table
        # which represent the minimum number of edits required
        # to convert an empty string to a non-empty prefix of
        # the input strings
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0:
                    dp[i][j] = j  # Need to insert `j` chars to become word2[:j]
                elif j == 0:
                    dp[i][j] = i  # Need to delete `i` chars to become ""
        
        # Fill in the rest of the dp table
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    # No edit needed if characters are the same
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Find the minimum of the three possible edits:
                    # 1. Insert a character in word1 to match word2[j]
                    # 2. Delete a character from word1 to match word2[:j-1]
                    # 3. Replace a character in word1 with word2[j]
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        # The last element of the dp table represents the minimum number
        # of edits required to convert the entire word1 to word2
        return dp[len1][len2]
