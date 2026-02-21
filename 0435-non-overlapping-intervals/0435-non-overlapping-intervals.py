class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        count = 0

        for start, end in intervals[1:]:
            if start < merged[-1][1]:
                merged[-1][1] = min(merged[-1][1], end)
                count += 1
            else:
                merged.append([start, end])

        return count