class Solution:
    def solve(self, index, total, brackets, res):
        if index >= len(brackets):  # base case
            if total == 0: # toatl jb 0 hoga yaani equal brackets open or close hua
                res.append("".join(brackets))
            return
        if total > len(brackets)//2:  # agar total bada ho jayega yaani equal brackets nhi hua kuchh km kuchh zyada
            return
        elif total < 0:  # total negative ka mtlb close se start hoga to koi fayeda hi nhi
            return 
        brackets[index] = "("  # start kr rhe h
        curr_sum = total + 1  # total ko badhaya
        self.solve(index+1, curr_sum, brackets, res)
        brackets[index] = ")"  # ab change hua open se close
        curr_sum = total - 1  # or jab close hua to total ko ghatayenge
        self.solve(index+1, curr_sum, brackets, res)
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (n*2)  # kyun ki n ka doguna hoga brackets
        res = []
        self.solve(0, 0, brackets, res)
        return res