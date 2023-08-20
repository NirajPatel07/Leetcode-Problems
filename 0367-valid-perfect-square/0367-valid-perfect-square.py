class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l<=r:
            mid = (l+r)//2
            sq = mid**2
            if sq == num:
                return True
            elif sq>num:
                r = mid-1
            else:
                l = mid+1
        return False