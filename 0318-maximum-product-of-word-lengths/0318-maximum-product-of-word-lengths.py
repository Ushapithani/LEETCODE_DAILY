class Solution:
    def maxProduct(self, words: list[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res