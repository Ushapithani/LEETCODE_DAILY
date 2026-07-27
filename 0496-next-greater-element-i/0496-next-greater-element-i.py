class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mapping = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            if num in mapping:
                res.append(mapping[num])
            else:
                res.append(-1)
        return res