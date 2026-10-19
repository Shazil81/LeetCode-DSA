class Solution:
    def solve(self, index1, index2, s1, s2, dp): 
        if index1 < 0:
            return index2 + 1
        if index2 < 0:
            return index1 + 1

        if dp[index1][index2] != -1:
            return dp[index1][index2]

        if s1[index1] == s2[index2]:
            dp[index1][index2] = self.solve(index1-1, index2-1, s1, s2, dp)
        else:
            insert = self.solve(index1, index2-1, s1, s2, dp)
            delete = self.solve(index1-1, index2, s1, s2, dp)
            replace = self.solve(index1-1, index2-1, s1, s2, dp)
            dp[index1][index2] = 1 + min(insert, delete, replace)

        return dp[index1][index2]


    def minDistance(self, word1: str, word2: str) -> int:
        # hmko min operations count krna hai
        # hum word1 ko word2 bna rhe h or uska min cost le rhe h
        n1, n2 = len(word1), len(word2)
        dp = [[-1] * n2 for _ in range(n1)]
        return self.solve(n1-1, n2-1, word1, word2, dp)