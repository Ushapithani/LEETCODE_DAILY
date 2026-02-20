class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        def helper(s, num):
            if not s or not s[0].isdigit():
                return num
            return helper(s[1:], num * 10 + int(s[0]))
        
        num = sign * helper(s, 0)
        return max(-2**31, min(2**31 - 1, num))

