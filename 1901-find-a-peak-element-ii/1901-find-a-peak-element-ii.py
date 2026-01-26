class Solution:
    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            max_row = 0
            for r in range(m):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r

            mid_val = mat[max_row][mid]

            if mid - 1 >= 0:
                left_val = mat[max_row][mid - 1]
            else:
                left_val = -1

            if mid + 1 < n:
                right_val = mat[max_row][mid + 1]
            else:
                right_val = -1

            if mid_val > left_val and mid_val > right_val:
                return [max_row, mid]
            elif right_val > mid_val:
                left = mid + 1
            else:
                right = mid - 1