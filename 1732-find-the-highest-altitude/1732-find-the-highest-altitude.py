class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = alt = 0
        
        for g in gain:
            alt += g
            ans = max(ans,alt)
        return ans