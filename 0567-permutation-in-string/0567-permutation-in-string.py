class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Length of s1 and s2
        len_s1, len_s2 = len(s1), len(s2)
        
        # Counter of s1 and initial window of s2
        char_count_s1, char_count_window = Counter(s1), Counter(s2[:len_s1])
        
        # Loop remaining characters of s2
        for i in range(len_s1, len_s2):
            # Return True if s1 is a permutation of window
            if char_count_s1 == char_count_window:
                return True
            
            # Move window by removing prev and adding curr character
            char_count_window[s2[i - len_s1]] -= 1
            char_count_window[s2[i]] += 1
        
        # Return result of comparison between char_count_s1 and char_count_window
        return char_count_s1 == char_count_window
