class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subseq(word, s):
            i = 0
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
            return i == len(word)
        
        res = ""
        for word in dictionary:
            if is_subseq(word, s):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res