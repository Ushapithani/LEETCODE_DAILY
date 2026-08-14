class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        vowel_list = []

        for ch in s:
            if ch in vowels:
                vowel_list.append(ch)

        vowel_list.reverse()

        result = []
        index = 0

        for ch in s:
            if ch in vowels:
                result.append(vowel_list[index])
                index += 1
            else:
                result.append(ch)

        return "".join(result)