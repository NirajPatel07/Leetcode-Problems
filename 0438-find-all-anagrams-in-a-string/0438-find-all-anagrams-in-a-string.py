class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        # count of chars in target
        p_count = Counter(p) 
        
        # count of chars in initial window of source string
        s_window_count = Counter(s[:len(p)])  
        
        # loop through source string to compare each window with target
        for i in range(len(s) - len(p)):
            if p_count == s_window_count:
                res.append(i)

            # decrement count for the char which is left out of the window
            s_window_count[s[i]] -= 1

            # remove char count if it becomes zero
            if s_window_count[s[i]] == 0:
                del s_window_count[s[i]]

            # increment count for the char which is included in the window
            s_window_count[s[i + len(p)]] += 1

        # check if last window is anagram or not
        if p_count == s_window_count:
            res.append(len(s) - len(p))
            
        return res
