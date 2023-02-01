class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        l = r = 0
        
        w = 0
        while(l<=r and r<len(blocks)):
            if blocks[r] != 'B':
                w += 1
            if r-l+1 == k:
                ans = min(ans,w)
                r = l
                l += 1
                w = 0
        
            r += 1
        return ans  