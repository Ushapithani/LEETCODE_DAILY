class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        count = {}

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for num in seen:
                if num not in count:
                    count[num] = 0

                count[num] += 1

        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans