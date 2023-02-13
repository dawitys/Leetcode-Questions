class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp = [inf] * len(coins)
        
        while(coins > 0):
            
            
        return min(dp)
        recursive relation

        '''
        @cache
        def dfs(rem):
            if rem < 0:
                return inf
            if rem == 0:
                return 0
            better = inf
            for c in coins:
                better = min(better,dfs(rem-c)+1)
            
            return better 
        res = dfs(amount)
        return res if res != inf else -1
            