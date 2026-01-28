class Solution:
    def mostFrequent(self, nums, key):
        freq = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                nxt = nums[i + 1]
                if nxt in freq:
                    freq[nxt] += 1
                else:
                    freq[nxt] = 1
        return max(freq, key=freq.get)