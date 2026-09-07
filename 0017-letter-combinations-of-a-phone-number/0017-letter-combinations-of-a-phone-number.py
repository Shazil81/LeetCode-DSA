class Solution:
    def solve(self, index, digits, subset, char_map, res):
        if index >= len(digits): # base condition
            res.append("".join(subset)) # kyun ki string chahiye isi liye list ko string bnaya
            return
        
        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.solve(index+1, digits, subset, char_map, res)
            subset.pop()
        

    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"} # ye char_map is liye bnaya h ki access kr sken 
        res = []
        self.solve(0, digits, [], char_map, res)
        return res
