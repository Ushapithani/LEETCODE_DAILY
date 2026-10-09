
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        op = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                op += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                if op > 0:
                    op -= 1
                else:
                    ans += 1

            i += 1

        ans += op * 2
        return ans