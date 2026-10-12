class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        b=[" "]*len(s)
        for i in range(len(s)):
            b[indices[i]]=s[i]
        return "".join(b)