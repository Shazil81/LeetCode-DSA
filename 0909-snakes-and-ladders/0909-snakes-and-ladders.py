from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        queue = deque([(1,0)])  # curr_square, moves
        vis = set([1])

        while queue:
            curr, moves = queue.popleft()

            if curr == n * n:  # target pe agar phuncha to return
                return moves
            
            for dice in range(1, 7):
                next_square = curr + dice
                if next_square > n * n:
                    break
                
                row = n - 1 - (next_square - 1) // n  # Row calc kr rhe hai
                col = (next_square - 1) % n

                if (n - row) % 2 == 0: # col agar even hai tab
                    col = n - 1 - col  

                if board[row][col] != -1: 
                    dest = board[row][col] 
                else:
                    dest = next_square
                
                if dest not in vis:
                    vis.add(dest)
                    queue.append((dest, moves + 1))
        
        return -1
