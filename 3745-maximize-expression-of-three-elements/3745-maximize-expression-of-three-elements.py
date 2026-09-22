class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        largest = float("-inf")
        second_largest = float("-inf")
        smallest = float("inf")

        for num in nums:
            if num < smallest:
                smallest = num

            if num >= largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num

        return largest + second_largest - smallest