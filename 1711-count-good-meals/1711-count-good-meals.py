class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        
        counter = Counter()
        ans = 0
        for d in deliciousness:
            for i in range(22):
                ans += counter[(1 << i) - d] % MOD
            counter[d] += 1    
        return ans % MOD