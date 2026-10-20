
class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                if int(digits[i]) % 2 == int(digits[j]) % 2:
                    if digits[i] < digits[j]:
                        digits[i], digits[j] = digits[j], digits[i]

        return int("".join(digits))
