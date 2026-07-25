class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi  = 0 
        for sent in sentences:
            words = sent.split()
            maxi = max(maxi,len(words))
        return maxi 
        