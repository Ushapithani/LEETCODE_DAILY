class Solution:
    def longestWord(self, words):
        words.sort()
        valid_words = set([""])
        longest_word = ""

        for current_word in words:

            if current_word[:-1] in valid_words:
                valid_words.add(current_word)
                
                if len(current_word) > len(longest_word):
                    longest_word = current_word

        return longest_word