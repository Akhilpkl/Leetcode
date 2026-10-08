class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        o=""
        t=""
        for i in word1:
            o+=i
        for i in word2:
            t+=i
        if o==t:
            return True
        else:
            return False
        