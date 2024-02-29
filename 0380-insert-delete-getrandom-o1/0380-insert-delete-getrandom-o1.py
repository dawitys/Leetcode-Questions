import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.seen = {}

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        self.data.append(val)
        self.seen[val] = len(self.data)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False
        cidx = self.seen[val]
        self.seen[self.data[-1]] = cidx
        self.data[cidx],self.data[-1] = self.data[-1],self.data[cidx]
        self.data.pop()
        del self.seen[val]
        return True

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.data)-1)
        return self.data[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()