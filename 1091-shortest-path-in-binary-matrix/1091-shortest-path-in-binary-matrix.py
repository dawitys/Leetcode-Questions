class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1 :
            return -1
        
        DIRS = [[1,0],[0,1],[1,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1]]
        
        q = deque()
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        q.append((0,0,1))
        
        def inbound(x,y):
            return 0<=x< len(grid) and 0<=y<len(grid[0])
        
        while q:
            cx,cy, d = q.popleft()
            if cx == len(grid)-1 and cy == len(grid[0])-1:
                return d
            for dx, dy in DIRS:
                nx,ny = cx + dx, cy + dy
                if inbound(nx,ny) and grid[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx,ny,d+1))
                    visited[nx][ny] = True 
        return -1