class Solution:

    def __init__(self, w):
        self.prefix = list(accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.prefix, random.randint(1, self.prefix[-1]))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()