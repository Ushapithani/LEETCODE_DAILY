class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        changed = True
        while changed:
            changed = False 
            for i in range(len(s)):
                for j in range(i+1, min(i+k+1, len(s))):
                    if s[i] == s[j]:
                        s = s[:j] + s[j+1:]
                        changed = True
                        break
                if changed:
                    break
        return s 
        