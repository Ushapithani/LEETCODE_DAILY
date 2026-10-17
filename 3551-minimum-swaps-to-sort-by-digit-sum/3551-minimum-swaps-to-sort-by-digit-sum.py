class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []

        for i in range(len(nums)):
            n = nums[i]
            total = 0

            while n > 0:
                total += n % 10
                n //= 10

            arr.append((total, nums[i], i))

        arr.sort()

        swaps = 0

        for i in range(len(arr)):
            while arr[i][2] != i:
                j = arr[i][2]
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        return swaps