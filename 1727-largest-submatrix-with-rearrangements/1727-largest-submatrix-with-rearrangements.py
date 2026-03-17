class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        ans = 0

        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            for k, h in enumerate(row):
                if h == 0:
                    break
                ans = max(ans, h * (k + 1))

        return ans