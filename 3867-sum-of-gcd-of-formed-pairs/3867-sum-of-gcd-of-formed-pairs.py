class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        from math import gcd 
        vel = nums
        prefixgcd = []
        mx = 0 
        for i in range(len(nums)):
            mx = max(mx,vel[i])
            prefixgcd.append(gcd(vel[i],mx))

        prefixgcd.sort()

        left = 0 
        right = len(prefixgcd)-1
        total = 0 
        while left < right:
            total+=gcd(prefixgcd[left],prefixgcd[right])
            left+=1
            right-=1
        return total 