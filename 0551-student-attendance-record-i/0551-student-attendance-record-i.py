class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0 
        absent = 0 
        for ch in s:
            if ch=='A':
                absent+=1
                if absent>=2:
                    return False
                late = 0 
            elif ch =="L":
                late+=1
                if late>=3:
                    return False
            else:
                late=0
        return True



        