class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        print(bin(a),bin(b),bin(c))
        
        for i in range(32):
            if (((a&1<<i) | (b&1<<i) == 0) and (c&1<<i != 0)) :
                count += 1
            elif (((a&1<<i) & (b&1<<i) != 0) and (c&1<<i == 0)): 
                count += 2
            elif (((a&1<<i) | (b&1<<i) != 0) and (c&1<<i == 0)) :
                count += 1
        
        return count