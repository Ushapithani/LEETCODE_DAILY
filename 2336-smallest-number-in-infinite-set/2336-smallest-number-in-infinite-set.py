class SmallestInfiniteSet:

    def __init__(self):
        self.nums = list(range(1,1001))
        

    def popSmallest(self) -> int:
        return self.nums.pop(0)
        

    def addBack(self, num: int) -> None:
        if num not in self.nums :
            self.nums.append(num)
            self.nums.sort()

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)