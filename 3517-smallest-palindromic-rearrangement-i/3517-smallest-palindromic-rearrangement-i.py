class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s = sorted(s)

        first = ""
        middle = ""

        i = 0
        while i < len(s):
            count = 1

            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1

            first += s[i] * (count // 2)

            if count % 2 == 1:
                middle = s[i]

            i += 1

        return first + middle + first[::-1]