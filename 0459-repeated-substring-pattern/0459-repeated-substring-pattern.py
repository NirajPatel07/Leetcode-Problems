class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep_str = ''
        s_len = len(s)
        
        for i in range(s_len // 2):
            rep_str += s[i]
            
            if s_len % len(rep_str) == 0:
                if rep_str * (s_len // len(rep_str)) == s:
                    return True
                
        return False