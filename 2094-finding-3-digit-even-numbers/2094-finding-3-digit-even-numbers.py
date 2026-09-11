class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        res = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i != j and j != k and k != i:

                        num = digits[i] * 100 + digits[j] * 10 + digits[k]

                        if num >= 100 and num % 2 == 0:
                            res.add(num)

        return sorted(res)