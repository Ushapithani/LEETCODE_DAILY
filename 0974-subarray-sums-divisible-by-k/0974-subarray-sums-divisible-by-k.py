class Solution:
    def subarraysDivByK(self, nums, k):
        mp = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            rem = prefix % k

            if rem < 0:
                rem += k

            if rem in mp:
                ans += mp[rem]
                mp[rem] += 1
            else:
                mp[rem] = 1

        return ans