class Solution:
    def reverseDegree(self, s):
        total = 0

        for i in range(len(s)):
            value = ord(s[i]) - ord('a') + 1
            reverse_value = 27 - value

            total += reverse_value * (i + 1)

        return total