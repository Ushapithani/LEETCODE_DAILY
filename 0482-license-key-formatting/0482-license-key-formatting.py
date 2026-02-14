class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        initial_size = len(s)%k or k 
        res = s[:initial_size]

        for i in range(initial_size, len(s), k):
            res+= "-"+ s [i:i+k]
        return res
        