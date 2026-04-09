class Solution:
    def findRelativeRanks(self, score):
        res = [""] * len(score)
        sorted_scores = sorted(score, reverse=True)
        
        for i, s in enumerate(sorted_scores):
            if i == 0:
                res[score.index(s)] = "Gold Medal"
            elif i == 1:
                res[score.index(s)] = "Silver Medal"
            elif i == 2:
                res[score.index(s)] = "Bronze Medal"
            else:
                res[score.index(s)] = str(i + 1)
        
        return res