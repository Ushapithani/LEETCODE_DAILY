class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = sys.maxsize
        for x in nums :
            if x <= first:
                first = x 
            elif x <= second :
                second = x
            else :
                return True 
        return False
    