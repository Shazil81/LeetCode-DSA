class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def solve(index, path, prev_num, curr_val):
            # Base Case
            if index == len(num):
                if curr_val == target:
                    res.append(path)
                return
            
            for i in range(index, len(num)):
                if i > index and num[index] == '0': # Leading zeros
                    break
                
                curr_str = num[index : i + 1]
                curr = int(curr_str)

                if index == 0:
                    solve(i + 1, curr_str, curr, curr)
                
                else:
                    # Add
                    solve(i+1, path + "+" + curr_str, curr, curr_val + curr)

                    # Substract
                    solve(i+1, path + "-" + curr_str, -curr, curr_val - curr)

                    # Multiply
                    solve(i + 1, path + "*" + curr_str, prev_num * curr, curr_val - prev_num + (prev_num * curr))
        
        solve(0, "", 0, 0)
        return res