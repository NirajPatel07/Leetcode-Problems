#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            print('*'*i, end='')
            print(' '*((N-i)*2), end='')
            print('*'*i, end='')
            print()
            
        
        for i in range(1, N+1):
            print('*'*i, end='')
            print(' '*((N-i)*2), end='')
            print('*'*i, end='')
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