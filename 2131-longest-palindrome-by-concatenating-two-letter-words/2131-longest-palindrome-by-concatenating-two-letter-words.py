from collections import Counter

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        count = Counter(words)
        length = 0
        center = False

        for word in count:
            rev = word[::-1]
            if word == rev:
                length += (count[word] // 2) * 4
                if count[word] % 2 == 1:
                    center = True
            elif word < rev:
                length += min(count[word], count[rev]) * 4

        if center:
            length += 2

        return length