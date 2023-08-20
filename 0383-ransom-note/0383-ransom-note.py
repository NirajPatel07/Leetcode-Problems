class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        
        for n in r_counter:
            if n in m_counter and m_counter[n] >= r_counter[n]:
                continue
            else:
                return False
            
        return True