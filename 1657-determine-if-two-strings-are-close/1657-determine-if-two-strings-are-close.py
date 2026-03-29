class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        c1 = Counter(word1)
        c2 = Counter(word2)
        return set(c1.keys()) and set(c2.keys()) and sorted(c1.values())==sorted(c2.values())

        