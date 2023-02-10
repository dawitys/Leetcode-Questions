class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        
        def inbound(i,j):
            return 0 <= i < n and 0 <= j <m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
        ans = -1
        visited = set()           
        while queue:
            ci,cj,dist = queue.popleft()
            ans = max(ans,dist)
            
            for ni,nj in [[ci,cj+1],[ci+1,cj],[ci,cj-1],[ci-1,cj]]:
                if inbound(ni,nj) and (ni,nj) not in visited and grid[ni][nj] == 0:
                    queue.append((ni,nj,dist+1))
                    visited.add((ni,nj))
            
        return ans if visited else -1