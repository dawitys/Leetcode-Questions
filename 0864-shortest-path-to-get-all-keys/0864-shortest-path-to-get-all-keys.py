class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        start = (-1,-1,0,0)  
        allkeys = 0
        def inbound(x,y):
            return 0 <= x < n and 0 <= y < m     
        
        for i in range(n):
            for j in range(m):
                if ord('a') <= ord(grid[i][j]) <= ord('z'):
                    key = ord(grid[i][j])-ord('a')+1
                    allkeys |= 1<<key
                if grid[i][j] == '@':
                    start = (i,j,0,0)

        queue = deque([start])
        visited = {(start[0],start[1],start[2])}
        
        while queue:

            cx,cy,mask,steps = queue.popleft()
            if mask == allkeys:
                return steps
            
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx,ny = cx + dx, cy + dy
                if inbound(nx,ny) and grid[nx][ny] != '#':
                    if grid[nx][ny] in '@.' and (nx,ny,mask) not in visited:
                        queue.append((nx,ny,mask,steps+1))
                        visited.add((nx,ny,mask))
                        
                    elif ord('a') <= ord(grid[nx][ny]) <=ord( 'z'):
                        key = ord(grid[nx][ny])-ord('a')+1
                        if (nx,ny,mask| 1<<key) not in visited:
                            queue.append((nx,ny,mask| 1<<key, steps+1))
                            visited.add((nx,ny,mask| 1<<key))
                    elif ord('A') <= ord(grid[nx][ny]) <=ord( 'Z'):
                        key = ord(grid[nx][ny])-ord('A')+1
                        if mask & 1<<key and (nx,ny,mask) not in visited:
                            queue.append((nx,ny,mask,steps+1))
                            visited.add((nx,ny,mask))
                            
        return -1
                        