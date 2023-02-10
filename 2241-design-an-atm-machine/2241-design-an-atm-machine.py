class ATM:

    def __init__(self):
        self.notes = [0]*5
        self.values = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0]* 5
        for i in range(4,-1,-1):
            c = (amount//self.values[i])
            if c <= self.notes[i]:
                amount = amount % self.values[i]
                res[i] = c
            else:
                amount -= self.notes[i] * self.values[i]
                res[i] = self.notes[i]
        if amount == 0:
            for i in range(4,-1,-1):
                self.notes[i] -= res[i]
            return res
        return [-1]
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)