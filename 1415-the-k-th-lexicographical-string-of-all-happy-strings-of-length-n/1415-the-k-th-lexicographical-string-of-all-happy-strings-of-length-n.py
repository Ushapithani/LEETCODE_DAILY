class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2 ** (n - 1))
        
        if k > total_happy:
            return ""
        
        res = []
        left, right = 1, total_happy

        for i in range(n):
            if i == 0:
                choices = "abc"
            else:
                choices = "abc".replace(res[-1], "")
            
            cur = left
            partition_size = (right - left + 1) // len(choices)

            for c in choices:
                if cur <= k < cur + partition_size:
                    res.append(c)
                    left, right = cur, cur + partition_size - 1
                    break
                cur += partition_size

        return "".join(res)