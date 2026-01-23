from collections import Counter

class Solution:
    def kthDistinct(self, arr, k):
        freq = Counter(arr)
        distinct = []
        for word in arr:
            if freq[word] == 1:
                distinct.append(word)
        if k <= len(distinct):
            return distinct[k-1]
        return ""