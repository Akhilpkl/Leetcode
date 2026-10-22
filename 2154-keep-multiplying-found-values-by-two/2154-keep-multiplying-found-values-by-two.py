class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        og=original
        while og in nums:
             og*=2
        return og