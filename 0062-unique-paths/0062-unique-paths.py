class Solution:
    dp = dict()
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            r = m
            c = n
        else:
            r = n
            c = m
            
        if r == 1 or c == 1:
            return 1

        if (r, c) not in self.dp:
            self.dp[(r, c)] = self.uniquePaths(r - 1, c) + self.uniquePaths(r, c - 1)

        return self.dp[(r,c)]