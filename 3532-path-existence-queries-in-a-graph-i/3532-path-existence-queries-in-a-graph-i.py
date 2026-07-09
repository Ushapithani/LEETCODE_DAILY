class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        group = [0] * n
        gid = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                gid += 1
            group[i] = gid

        return [group[u] == group[v] for u, v in queries]