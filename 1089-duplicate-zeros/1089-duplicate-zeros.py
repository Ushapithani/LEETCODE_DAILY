class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        for _ in range(len(arr)):
            if i >= len(arr):
                break
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 1
            i += 1