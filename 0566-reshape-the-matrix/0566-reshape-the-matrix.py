class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        # 1. Validation check
        if row * col != r * c:
            return mat

        k = 0
        res = []

        for i in range(r):
            lst = []
            for j in range(c):
                lst.append(mat[k // col][k % col])  # Ye formula hai isse 1-d coordinates se 2d me convert hota hai
                k += 1
            res.append(lst)
        
        return res
        