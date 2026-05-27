class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        first_upper = {}
        last_lower = {}

        for i in range(len(word)):

            if word[i].islower():
                last_lower[word[i]] = i

            else:
                ch = word[i].lower()

                if ch not in first_upper:
                    first_upper[ch] = i

        count = 0

        for ch in last_lower:

            if ch in first_upper:

                if last_lower[ch] < first_upper[ch]:
                    count += 1
                else:
                    pass

        return count