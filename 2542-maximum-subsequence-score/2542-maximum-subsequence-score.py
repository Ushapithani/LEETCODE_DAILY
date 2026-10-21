import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        min_heap = []
        curr_sum = 0 
        max_score = 0 
        
        for num2, num1 in pairs:
            heapq.heappush(min_heap, num1)
            curr_sum += num1
            
            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)
                
            if len(min_heap) == k:
                max_score = max(max_score, curr_sum * num2)
                
        return max_score