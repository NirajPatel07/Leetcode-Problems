class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        mod = 10**9 + 7
        n = len(arr)
        arr.sort()
        dp = [1]*n 
        for i in range(1,n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    temp = arr[i] // arr[j]
                    try: k = arr.index(temp)
                    except: continue
                    dp[i] += (dp[j] * dp[k])
        return sum(dp) % mod