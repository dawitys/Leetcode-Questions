class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0,0,1)])
        visited = {(0,0)}
        if grid[0][0] != 0:
            return -1
        n,m = len(grid), len(grid[0])
        
        def inBound(i,j):
            return 0 <= i < n and 0 <= j < m
        
        while(queue):
            ci,cj,length = queue.popleft()
            if ci == n-1 and cj == m-1:
                return length
            for i,j in [[ci+1,cj],[ci,cj+1],[ci-1,cj],[ci,cj-1],[ci+1,cj+1],[ci+1,cj-1],[ci-1,cj+1],[ci-1,cj-1]]:
                if inBound(i,j) and grid[i][j] == 0 and (i,j) not in visited:
                    queue.append((i,j,length+1))
                    visited.add((i,j))
        
        return -1