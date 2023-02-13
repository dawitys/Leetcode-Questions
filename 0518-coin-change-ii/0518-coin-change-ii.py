class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(rem,idx,cache):
            if (rem,idx) in cache:
                return cache[(rem,idx)]
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            ways = 0
            for i in range(idx, len(coins)):
                if rem >= coins[i]:
                    ways += dfs(rem-coins[i],i,cache)
                    
            cache[(rem,idx)] = ways
            return ways
        return dfs(amount,0,cache)