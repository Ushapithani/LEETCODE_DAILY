class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count = {}

        for ch in word1:
            count[ch] = count.get(ch, 0) + 1

        for ch in word2:
            count[ch] = count.get(ch, 0) - 1

        for ch in count:
            if abs(count[ch]) > 3:
                return False

        return True