class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # This is another method
        res = ""
        base = strs[0]
        for i in range(len(base)):
            for word in range(1, len(strs)):
                if i==len(strs[word]) or strs[word][i] != base[i]:
                    return res
            res+=base[i]
        return res 