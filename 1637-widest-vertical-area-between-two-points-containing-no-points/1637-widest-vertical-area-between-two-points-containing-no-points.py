class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        y = sorted([i for i,j in points])
        temp = ans = 0
        for i in range(1,len(y)):
            temp = y[i] - y[i-1]
            ans = max(temp,ans)
        return ans