class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        maxw = maxh = -math.inf
        for i in range(1,len(horizontalCuts)):
            maxw = max(maxw,horizontalCuts[i] - horizontalCuts[i-1])
                
        for j in range(1,len(verticalCuts)):
            maxh = max(verticalCuts[j] - verticalCuts[j-1],maxh)
            
        return maxh*maxw %  1000000007