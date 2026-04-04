
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        chars = sorted(count,key=count.get,reverse = True)
        return "".join(c*count[c] for c in chars)

        