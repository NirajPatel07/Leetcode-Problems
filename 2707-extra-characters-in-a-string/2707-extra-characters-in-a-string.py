class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache

        def dfs(s):
            if not s:
                return 0
            ans=inf
            for i in range(len(s)):
                sub=s[:i+1]
                if sub in seen:
                    ans=min(ans,dfs(s[i+1:]))
                else:
                    ans=min(ans,len(sub)+dfs(s[i+1:]))
            return ans
        
        seen=set(dictionary)
        return dfs(s)