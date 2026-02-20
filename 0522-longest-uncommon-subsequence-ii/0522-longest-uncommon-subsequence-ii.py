class Solution:
    def findLUSlength(self, strs):
        def is_subseq(s, t):
            i = 0
            for c in t:
                if i < len(s) and c == s[i]:
                    i += 1
            return i == len(s)
        
        res = -1
        for i in range(len(strs)):
            uncommon = True
            for j in range(len(strs)):
                if i != j and is_subseq(strs[i], strs[j]):
                    uncommon = False
                    break
            if uncommon:
                res = max(res, len(strs[i]))
        return res