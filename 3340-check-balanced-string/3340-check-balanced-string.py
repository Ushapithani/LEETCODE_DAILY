class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0

        for i, digit in enumerate(num):
            if i % 2 == 0:
                even += int(digit)
            else:
                odd += int(digit)

        return even == odd