class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={}
        for p in pieces:
            d[p[0]]=p
        i=0 
        while i < len(arr):
            if arr[i] not in d:
                return False
            piece=d[arr[i]]
            for x in piece:
                if arr[i]!=x:
                    return False
                i+=1
        return True


        