class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        
        for i in range(length):
            
            if i == 0:
                left = 0
            else:
                left = flowerbed[i - 1]
            
            if i == length - 1:
                right = 0
            else:
                right = flowerbed[i + 1]
            
            if flowerbed[i] == 0 and left == 0 and right == 0:
                flowerbed[i] = 1
                n = n - 1
                
                if n == 0:
                    return True
        
        return n <= 0