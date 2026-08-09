class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_sum = sum(map(int, num[1::2]))
        even_sum = sum(map(int, num[::2]))
        return odd_sum == even_sum