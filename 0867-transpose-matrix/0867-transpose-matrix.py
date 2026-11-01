class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # matrix[r][c] ban jayega matrix[c][r]

        row = len(matrix)
        col = len(matrix[0])
        mat = [[0]*row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                mat[j][i] = matrix[i][j]
        
        return mat

