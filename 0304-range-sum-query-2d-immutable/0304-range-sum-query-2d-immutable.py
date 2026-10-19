class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.P[i+1][j+1] = (matrix[i][j]
                                    + self.P[i][j+1] # upar wala rect
                                    + self.P[i+1][j] # left wala rect
                                    - self.P[i][j])  # overlap wala rect

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        P = self.P
        return (P[row2+1][col2+1]
                - P[row1][col2+1]  # upar wala ko minus kiya
                - P[row2+1][col1]  # left wala ko minus kiya
                + P[row1][col1])   # corner wapas se add kro kyun ki 2 baar hat gya hai


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)