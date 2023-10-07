class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(index,val,cost):
            if index == n:
                if cost == k:
                    return 1
                return 0
            ans = max(0,val*dp(index+1,val,cost))
            for newval in range(val+1,m+1):
                ans+=dp(index+1,newval,cost+1)
            return ans%MOD
        return dp(0,0,0)