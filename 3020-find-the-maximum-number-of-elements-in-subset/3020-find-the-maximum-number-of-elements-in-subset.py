from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        if 1 in cnt:
            ans = cnt[1] if cnt[1] % 2 == 1 else cnt[1] - 1

        max_num = max(nums)

        for num in cnt:
            if num == 1:
                continue

            x = num
            length = 0

            while x <= max_num and cnt[x] >= 2:
                length += 2
                x *= x

            if x in cnt:
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length - 1)

        return ans