#User function Template for python3

class Solution:
    def printTriangle(self, N):
        k1 = N-1
        for i in range(1, N+1):
            print(' '*k1 + '* '*i)
            k1-=1
        
        k2=0
        for i in range(N, 0, -1):
            print(' '*k2 + '* '*i)
            k2+=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends