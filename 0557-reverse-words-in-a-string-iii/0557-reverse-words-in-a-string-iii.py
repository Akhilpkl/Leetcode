class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        return " ".join(wo[::-1] for wo in w)
        