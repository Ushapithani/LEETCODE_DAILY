class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for start in range(1, 9):
            num = start

            for next_digit in range(start + 1, 10):
                num = num * 10 + next_digit

                if low <= num <= high:
                    ans.append(num)

        ans.sort()
        return ans