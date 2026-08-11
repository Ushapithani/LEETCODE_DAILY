class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        chars = list(s)
        chars.sort(key=lambda x:(-freq[x],x))
        return ''.join(chars)