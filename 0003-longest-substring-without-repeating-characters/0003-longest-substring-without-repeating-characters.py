class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        op = 0
        st = ""
        
        for i in s:
            if i in st:
                st = st[st.index(i)+1:]
            st+=i
            op = max(len(st), op)
        return op