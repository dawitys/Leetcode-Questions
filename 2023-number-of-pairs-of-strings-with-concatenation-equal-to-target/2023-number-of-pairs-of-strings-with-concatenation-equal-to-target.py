class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        prefixes = Counter()
        suffices = Counter()
        
        for n in nums:
            if len(n) <= len(target) and n == target[:len(n)]:
                prefixes[n] += 1
            
            if len(n) <= len(target) and n == target[-len(n):]:
                suffices[n] += 1
                
        ans = 0
        for p in prefixes:
            for s in suffices:
                if len(p) + len(s) == len(target):
                    if s != p:
                        ans += (prefixes[p] * suffices[s])
                    else:
                        ans += prefixes[p] * (prefixes[p]-1)
                    
        return ans