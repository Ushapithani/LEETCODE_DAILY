class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        
        for word in words:
            valid = True
            for ch in word:
                if ch not in allowed_set:
                    valid = False
                    break
            if valid:
                count += 1
        
        return count