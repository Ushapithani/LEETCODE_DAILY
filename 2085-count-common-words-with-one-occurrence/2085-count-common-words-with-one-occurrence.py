from collections import Counter

class Solution:
    def countWords(self, words1, words2):
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        result = 0
        for word in freq1:
            if freq1[word] == 1 and freq2[word] == 1:
                result += 1
        return result