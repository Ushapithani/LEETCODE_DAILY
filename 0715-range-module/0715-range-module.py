class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        newRange = [left, right]
        result = []
        inserted = False

        for start, end in self.ranges:
            if end < newRange[0]:
                result.append([start, end])
            elif start > newRange[1]:
                if not inserted:
                    result.append(newRange)
                    inserted = True
                result.append([start, end])
            else:
                newRange[0] = min(newRange[0], start)
                newRange[1] = max(newRange[1], end)

        if not inserted:
            result.append(newRange)

        self.ranges = result

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