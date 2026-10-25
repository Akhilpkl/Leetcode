class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = 0
        max_area = 0

        for i in dimensions:
            l = i[0]
            w = i[1]

            d = l**2 + w**2
            area = l * w

            if d > max_d:
                max_d = d
                max_area = area
            elif d == max_d:
                max_area = max(max_area, area)

        return max_area