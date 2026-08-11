class Solution:
    def mostFrequentEven(self, nums):
        freq = {}

        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1

        if not freq:
            return -1

        return min(freq, key=lambda x: (-freq[x], x))