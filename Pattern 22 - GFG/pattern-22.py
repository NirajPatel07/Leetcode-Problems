#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,2*N):
            for j in range(1,2*N):
                if i>N:
                    i = 2*N - i
                if j>N:
                    j = 2*N - j
                print(N - min(i, j) + 1, end =' ')
            print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends