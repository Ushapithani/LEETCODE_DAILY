class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        result = 0

        for num in nums:
            prefix = (prefix + num) % k
            result += count[prefix]
            count[prefix] += 1

        return result