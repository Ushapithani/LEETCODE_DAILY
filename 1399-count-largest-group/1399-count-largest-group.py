
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for i in range(1, n + 1):
            num = i
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            if total not in groups:
                groups[total] = 0

            groups[total] += 1

        maximum = max(groups.values())
        count = 0

        for size in groups.values():
            if size == maximum:
                count += 1

        return count
