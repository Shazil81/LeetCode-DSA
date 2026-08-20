class Solution:
    def solve(self, index, currIp, s, res):
        # base case
        if len(currIp) == 4:
            if index == len(s):
                res.append(".".join(currIp))
            return
        # har part 1 se 3 digit lamba ho skta hai
        for length in range(1, 4):
            if index + length > len(s):
                break
            
            segment = s[index:index+length]
            if segment.startswith("0") and len(segment) > 1: # leading zeros check
                continue
            
            if int(segment) <= 255: # value check (0 - 255)
                currIp.append(segment)
                self.solve(index+length, currIp, s, res)
                currIp.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # base case
        if len(s) < 4 or len(s) > 12: # length 4 se 12 k bich me honi chahiye
            return res
        
        self.solve(0, [], s, res)
        return res
