
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        mp = {}

        for i in range(len(s)):
            c = s[i]

            if c not in mp:
                mp[c] = i
            else:
                d = i - mp[c] - 1
                idx = ord(c) - ord('a')

                if d != distance[idx]:
                    return False

        return True
