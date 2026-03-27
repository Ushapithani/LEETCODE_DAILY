class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        for i,(s,e) in enumerate(intervals):
            start.append((s,i))
        start.sort()
        def binary_search(target):
            low= 0 
            high =  len(start)-1
            ans = -1
            while low<=high:
                mid = (low+high)//2
                if start[mid][0]>=target:
                    ans = start[mid][1]
                    high = mid-1
                else:
                    low = mid+1
            return ans

        result = []
        for s ,e in intervals:
            result.append(binary_search(e))
        return result      