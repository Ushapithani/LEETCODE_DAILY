class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
        
        count = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
        
        return count