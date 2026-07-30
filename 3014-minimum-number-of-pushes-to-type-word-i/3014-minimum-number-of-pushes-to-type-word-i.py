class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        # Count frequency manually
        for ch in word:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        frequencies = sorted(freq.values(), reverse=True)

        pushes = 0

        for i in range(len(frequencies)):
            pushes += frequencies[i] * (i // 8 + 1)

        return pushes