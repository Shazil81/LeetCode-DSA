class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        res = []
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        for word in words:
            w = word.lower()
            # first char ka row check krna hoga us word ka
            if w[0] in row1:
                row = row1
            elif w[0] in row2:
                row = row2
            else:
                row = row3
            
            # ab har char usi row mein hona chahiye
            ok = True
            for ch in w:
                if ch not in row:
                    ok = False
                    break

            if ok:
                res.append(word)
        
        
        return res