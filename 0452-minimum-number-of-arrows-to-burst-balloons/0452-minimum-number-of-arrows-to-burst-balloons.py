class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        merged = [points[0]]

        for start, end in points[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = min(merged[-1][1], end)
            else:
                merged.append([start, end])

        return len(merged)