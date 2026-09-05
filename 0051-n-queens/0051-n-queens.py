class Solution:
    
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n): # ye hai solve wala
        if col == n: # base condition
            ans.append(list(board))
            return
        for row in range(n):
            if (
                leftrow[row] == 0
                and lowerDiagonal[row + col] == 0 # yhi formula se dega lower diagonal ka values
                and upperDiagonal[n - 1 + col - row] == 0 # yhi formula se dega upperDiagonal ka values
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftrow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                self.solve(col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
                # Now Backtrack
                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0
    def solveNQueens(self, n: int) -> List[List[str]]:
        # every row has 1 queen and every column has 1 queen only
        # no queen should hit each other

        board = ["." *n for _ in range(n)]
        ans = []
        leftrow = [0] * n
        upperDiagonal = [0] * (2* n - 1) # length
        lowerDiagonal = [0] * (2 * n -1)
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans





        