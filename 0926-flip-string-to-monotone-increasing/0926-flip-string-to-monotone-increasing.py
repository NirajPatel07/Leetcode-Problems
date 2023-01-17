class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = total_ones = 0

        for e in s:
            if e == '1':
                total_ones +=1
            else:
                flips = min(flips+1, total_ones)

        return flips