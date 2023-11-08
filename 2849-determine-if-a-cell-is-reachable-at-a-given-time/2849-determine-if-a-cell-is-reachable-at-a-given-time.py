class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        nx = abs(fx-sx)
        ny = abs(fy-sy)
        if nx == 0 and ny == 0 and t == 1:
            return False

        maxn = max(nx, ny)
        if t < maxn:
            return False
        return True