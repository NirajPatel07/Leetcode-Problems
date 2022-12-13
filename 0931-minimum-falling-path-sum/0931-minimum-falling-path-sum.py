class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        from functools import reduce
        padding = [float('inf')]
        def combine_rows(lower_row, upper_row):
            return [upper + min(lower_left, lower_mid, lower_right)
                    for upper, lower_left, lower_mid, lower_right in
                    zip(upper_row, lower_row[1:]+padding, lower_row, padding+lower_row[:-1])]
        return min(reduce(combine_rows, A[::-1]))