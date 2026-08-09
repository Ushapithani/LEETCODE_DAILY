class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        for num, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            if len(result) < k:
                result.append(num)

        return result