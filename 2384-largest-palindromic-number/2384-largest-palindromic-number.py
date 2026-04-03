class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1

        left = ""
        middle = ""

        for d in range(9, -1, -1):
            if d == 0 and left == "":
                continue
            pairs = freq[d] // 2
            left += str(d) * pairs

        for d in range(9, -1, -1):
            if freq[d] % 2 == 1:
                middle = str(d)
                break

        result = left + middle + left[::-1]

        return result if result else "0"