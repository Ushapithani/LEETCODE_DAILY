class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = ""
        for i in range(len(number)):
            if number[i]==digit:
                temp = number[:i]+number[i+1:]
                if temp>result:
                    result = temp 
        return result
        