class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        for ch in s:
            if ch.isalpha():
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2

        if k >= length:
            return '.'

        for ch in reversed(s):
            if ch.isalpha():
                length -= 1
                if k == length:
                    return ch

            elif ch == '*':
                length += 1

            elif ch == '#':
                length //= 2
                if k >= length:
                    k -= length

            elif ch == '%':
                k = length - 1 - k

        return '.'