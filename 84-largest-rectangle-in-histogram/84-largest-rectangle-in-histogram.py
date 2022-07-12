class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        '''
        heights.append(0)
        stack = [(-1,-1)]
        maxArea = 0
        
        for i,h in enumerate(heights):
            while(stack and stack[-1][0] > h):
                height,pos = stack.pop()
                maxArea = max(maxArea,(i-stack[-1][1]-1)*height)
            stack.append((h,i))
            
        return maxArea