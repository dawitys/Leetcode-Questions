class MyCircularQueue:

    def __init__(self, k):
        self.lst = [0] * k
        self.size, self.k = 0, k
        self.l = self.r = 0

    def enQueue(self, value):
        if not self.isFull():
            self.lst[self.r] = value
            self.r = (self.r+1) % self.k
            self.size += 1
            return True
        return False

    def deQueue(self):
        if not self.isEmpty():
            self.l = (self.l+1) % self.k
            self.size -= 1
            return True
        return False

    def Front(self):
        return self.lst[self.l] if self.size else -1

    def Rear(self):
        return self.lst[self.r-1] if self.size else -1
        

    def isEmpty(self):
        return True if not self.size else False
        

    def isFull(self):
        return True if self.size == self.k else False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()