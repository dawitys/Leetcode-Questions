class Solution:
    
    def detonates(self,i,j,bombs):
        return (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 <= bombs[i][2]**2
    
    def dfs(self,i,graph,visited):
        depth = 1
        for ne in graph[i]:
            if ne not in visited:
                visited.add(ne)
                depth += self.dfs(ne,graph,visited)
        return depth
        
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i != j and self.detonates(i,j,bombs):
                        graph[i].append(j)
                        
        max_detonation = 0
        for i in range(n):
            visited = {i}
            max_detonation = max(max_detonation,self.dfs(i,graph,visited))
            
        return max_detonation
                        