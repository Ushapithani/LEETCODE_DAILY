class Solution:
    def evaluate(self, s, knowledge):
        
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        ans = ""
        i = 0

        while i < len(s):

            if s[i] == '(':
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                ans += mp.get(key, "?")

                i = j + 1

            else:
                ans += s[i]
                i += 1

        return ans