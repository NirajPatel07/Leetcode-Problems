class Solution:
    def largestSubmatrix(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0

        for j in range(cols):
            cont_sum = 0
            for i in range(rows):
                if matrix[i][j] == 0:
                    cont_sum = 0
                    continue

                cont_sum += 1
                matrix[i][j] = cont_sum

        for i in range(rows):
            temp_list = sorted(matrix[i], reverse=True)

            for j in range(cols):
                max_area = max(max_area, (j + 1) * temp_list[j])

        return max_area