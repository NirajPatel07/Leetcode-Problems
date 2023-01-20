#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        N = n
        sum_n = 0
        while n:
            digit = n%10
            sum_n += pow(digit, 3)
            n = n//10
        if sum_n == N:
            return 'Yes'
        return 'No'
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends