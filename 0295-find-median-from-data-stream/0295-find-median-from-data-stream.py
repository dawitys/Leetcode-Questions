class MedianFinder:
    def __init__(self):
        self.lefts = []
        self.rights = []

    def addNum(self, num: int) -> None:
        heappush(self.rights,num)
        heappush(self.lefts,-heappop(self.rights))
        if len(self.lefts) > len(self.rights):
            heappush(self.rights, -heappop(self.lefts))

    def findMedian(self) -> float:
        return self.rights[0] if len(self.rights) > len(self.lefts) else  (- self.lefts[0] + self.rights[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()