# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        
        while left <= right:
            mid = (left + right)//2
            guess_n = guess(mid)
            if guess_n == 0:
                return mid
            elif guess_n == -1:
                right = mid -1
            else:
                left = mid + 1