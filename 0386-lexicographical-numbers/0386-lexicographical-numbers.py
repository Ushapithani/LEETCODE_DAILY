class Solution:

    def lexicalOrder(self, n: int) -> list[int]:

        l1 = []

        for i in range(1, n + 1):
            l1.append(str(i))

        l1.sort()

        l2 = []

        for item in l1:
            l2.append(int(item))

        return l2