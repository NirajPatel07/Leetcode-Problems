class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])

        for i in range(len(s) - len(p)):

            if p_counter == s_counter:
                res.append(i)

            s_counter[s[i]] -= 1

            if s_counter[s[i]] == 0:
                del s_counter[s[i]]

            s_counter[s[i + len(p)]] += 1

        if p_counter == s_counter:
            res.append(len(s) - len(p))
            
        return res