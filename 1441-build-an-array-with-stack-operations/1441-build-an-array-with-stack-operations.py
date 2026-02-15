from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        num = 1 
        
        for t in target:
            while num < t:
                result.append("Push")
                result.append("Pop")
                num += 1
            
            result.append("Push")
            num += 1
        
        return result