from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        letters = [ch.lower() for ch in licensePlate if ch.isalpha()]
        required = Counter(letters)
        result = None
        for word in words:
            word_count = Counter(word.lower())
            if all(word_count[char] >= required[char] for char in required):
                if result is None or len(word) < len(result):
                    result = word
        return result
