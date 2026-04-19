class Solution:
    def customSortString(self, order, s):
        pos = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: pos[x] if x in pos else 26))