class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strenght=[]
        for i in range(len(mat)):
            count = sum(mat[i])
            strenght.append((count,i))
        strenght.sort()
        result = []
        for i in range(k):
            result.append(strenght[i][1])
        return result