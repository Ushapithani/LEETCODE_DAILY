
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        
        for i in range(n):
            diagonal_char = nums[i][i]
            if diagonal_char == '0':
                result.append('1')
            else:
                result.append('0')
        
        return ''.join(result)