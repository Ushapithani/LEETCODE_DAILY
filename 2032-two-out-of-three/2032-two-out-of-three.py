class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        
        count = {}
        
        for num in s1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in s2:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in s3:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        result = []
        for num in count:
            if count[num] >= 2:
                result.append(num)
        
        return result