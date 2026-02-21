class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        self.ranges.append([left, right])
        self.ranges.sort(key=lambda x: x[0])
        merged = [self.ranges[0]]

        for start, end in self.ranges[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        self.ranges = merged

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        result = []

        for start, end in self.ranges:
            if end <= left or start >= right:
                result.append([start, end])
            else:
                if start < left:
                    result.append([start, left])
                if end > right:
                    result.append([right, end])

        self.ranges = result