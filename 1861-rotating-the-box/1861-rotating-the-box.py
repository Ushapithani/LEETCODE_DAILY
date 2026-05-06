class Solution:
    def rotateTheBox(self, box):
        m = len(box)
        n = len(box[0])

        for row in box:
            empty = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    empty = col - 1
                elif row[col] == '#':
                    row[col], row[empty] = '.', '#'
                    empty -= 1

        result = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box[i][j]

        return result