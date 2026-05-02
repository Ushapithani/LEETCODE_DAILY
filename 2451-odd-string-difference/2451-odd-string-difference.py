from collections import defaultdict

class Solution:
    def oddString(self, words):
        mp = defaultdict(list)

        for word in words:
            diff = []
            
            for i in range(len(word) - 1):
                diff.append(ord(word[i + 1]) - ord(word[i]))
            
            mp[tuple(diff)].append(word)

        for key in mp:
            if len(mp[key]) == 1:
                return mp[key][0]