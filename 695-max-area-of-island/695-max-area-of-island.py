class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inBound(x,y):
            return 0<= x<len(grid) and 0<=y<len(grid[0])
        
        DIRS = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        maxArea = 0
        
        def dfs(x,y):
            visited.add((x,y))
            area = 1
            for dx,dy in DIRS:
                nx,ny = x+dx,y+dy
                if inBound(nx,ny) and grid[nx][ny]==1 and (nx,ny) not in visited:
                    area += dfs(nx,ny)
            return area
        
        for i in range(len(grid)):
            for j in range( len(grid[0])):
                if grid[i][j]==1:
                    maxArea = max(maxArea,dfs(i,j))
        
        return maxArea