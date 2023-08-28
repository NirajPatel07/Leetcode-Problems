class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr_s = ''
        count = 0
        res = 0
        
        for c in s:
            if c not in curr_s:
                curr_s += c
                count += 1
            else:
                res = max(count, res)
                idx = curr_s.index(c)
                curr_s = curr_s[idx+1:] + c
                count = len(curr_s)
        
        return max(res, count)