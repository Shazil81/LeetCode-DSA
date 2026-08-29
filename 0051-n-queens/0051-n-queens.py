class Solution:
    def isSafe(self, row, col, board, n): # ye check krega ki no queens should attack each other
        duprow = row  # dummy use krega
        dupcol = col

        while row>=0 and col >= 0:  # diagonally pichhe me check krega upar side
            if board[row][col] == "Q":
                return False
            row-=1
            col-=1

        col = dupcol
        row = duprow

        while col >= 0: # pichhe straight check krega
            if board[row][col] == "Q":
                return False
            col-=1
        
        row = duprow
        col = dupcol

        while row < n and col >=0: # diagonally check krne k liye downwards me hoga
            if board[row][col] == "Q":
                return False
            row+=1
            col-=1
        return True
        
    
    def solve(self, col, board, ans, n): # ye hai solve wala
        if col == n: # base condition
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row, col, board, n): # jab true hai tb yaani queen attack nhi kr rha hoga
                # string immutable hai isi liye slicing ka use kr k hmko krna pad rha h
                # queen ko rakh rhe h jha pe vo safe hoga
                board[row] = board[row][:col] + "Q" + board[row][col+1:]  
                self.solve(col+1, board, ans, n)
                board[row] = board[row][:col] + "." + board[row][col+1:]
    def solveNQueens(self, n: int) -> List[List[str]]:
        # every row has 1 queen and every column has 1 queen only
        # no queen should hit each other
        # brute force se solve krte hain time O(N!*N)
        board = ["." *n for _ in range(n)]
        ans = []
        self.solve(0, board, ans, n)
        return ans





        