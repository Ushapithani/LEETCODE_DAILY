class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa, sb = set(), set()
        ans = []

        for i in range(len(A)):
            sa.add(A[i])
            sb.add(B[i])

            ans.append(len(sa & sb))

        return ans