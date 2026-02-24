class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        sorted_freq = sorted(freq, key=lambda x: freq[x], reverse=True)

        return sorted_freq[:k]