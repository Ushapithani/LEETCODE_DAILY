class Solution:
    def deleteAndEarn(self, nums):
        max_num = max(nums)

        points = [0] * (max_num + 1)

        for num in nums:
            points[num] += num

        prev = 0
        curr = 0

        for i in range(len(points)):
            next_points = max(curr, prev + points[i])
            prev = curr
            curr = next_points

        return curr