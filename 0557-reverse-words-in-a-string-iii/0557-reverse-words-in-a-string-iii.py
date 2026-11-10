class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        n = len(words)
        res = []
        for i in range(n):
            word = words[i]
            new_word = word[::-1]
            if i == n - 1:
                res.append(new_word)
            else:
                res.append(new_word + " ")
        
        return "".join(res)