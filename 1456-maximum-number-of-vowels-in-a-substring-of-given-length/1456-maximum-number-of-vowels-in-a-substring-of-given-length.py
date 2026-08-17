class Solution:
    def maxVowels(self, s, k):
        vowels = "aeiou"

        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            max_count = max(max_count, count)

        return max_count