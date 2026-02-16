import itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        perms = list(itertools.permutations(nums))
        return "".join(perms[k - 1])