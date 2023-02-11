#User function Template for python3

class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end = ' ')
        n = n-1
        return self.printNos(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends