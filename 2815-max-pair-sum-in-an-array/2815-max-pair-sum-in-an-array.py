class Solution:
    def maxSum(self, nums: List[int]) -> int:
        largest = [-1] * 10
        answer = -1

        for num in nums:
            max_digit = max(str(num))
            max_digit = int(max_digit)

            if largest[max_digit] != -1:
                answer = max(answer, num + largest[max_digit])

            largest[max_digit] = max(largest[max_digit], num)

        return answer