class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        
        for a in arr:
            counts[a] += 1
        
        for c in counts:
            if counts[c] > len(arr)/4:
                return c
