class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        ans = []
        
        for s in spells:
            ans.append(len(potions)-bisect.bisect_left(potions,success/s))
        
        return ans