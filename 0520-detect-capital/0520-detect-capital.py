class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.isupper():
            return True
        flag = True
        if word[0].isupper():
            for i in range(1, len(word)):
                if word[i].isupper(): 
                    flag = False
                    break
        
        if word[0].islower():
            for i in range(1, len(word)):
                if word[i].isupper(): # ya sirf pehla
                    flag = False
                    break
        
        return flag
        

