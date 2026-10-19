class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key =lambda x : x[1] ,reverse = True )
        total = 0 
        for box ,units in boxTypes:
            take = min(box,truckSize)
            total+=take*units
            truckSize-=take
            if truckSize ==0:
                break
        return total 
        