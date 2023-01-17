#User function Template for python3

class Solution:
    def printTriangle(self, N):
        odd_list = []
        
        i=1
        while len(odd_list)<N:
            odd_list.append(i)
            i+=2
        
        # print(odd_list)
        max_n = odd_list[-1]
        
        space = N-1
        i = 0
        while i<N:
            print(' '*space + '*'*odd_list[i])
            space-=1
            i+=1


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