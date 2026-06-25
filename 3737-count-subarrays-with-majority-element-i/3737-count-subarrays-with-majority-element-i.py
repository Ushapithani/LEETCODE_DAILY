class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            cnt_target = 0

            for j in range(i, n):
                if nums[j] == target:
                    cnt_target += 1

                length = j - i + 1

                if cnt_target > length // 2:
                    ans += 1

        return ans