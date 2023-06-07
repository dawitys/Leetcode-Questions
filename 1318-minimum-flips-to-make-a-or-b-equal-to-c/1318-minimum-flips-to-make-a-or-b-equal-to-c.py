class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        for i in range(32):
            if c & 1<<i:
                count += 0 if ((a & 1<<i) | (b & 1<<i)) else 1
            else:
                count += (a & 1<<i != 0) + (b & 1<<i != 0)
        
        return count