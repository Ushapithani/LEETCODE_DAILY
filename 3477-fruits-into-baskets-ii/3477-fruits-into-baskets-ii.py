class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        unplaced = 0

        for fruit in fruits:
            placed = False

            for i in range(n):
                if baskets[i] >= fruit:
                    baskets[i] = -1
                    placed = True
                    break

            if placed == False:
                unplaced += 1

        return unplaced