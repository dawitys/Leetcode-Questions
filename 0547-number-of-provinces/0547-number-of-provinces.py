class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node,visited):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour,visited)
        
        graph = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
              
        visited = set()
        provinces = 0
        for node in graph:
            if node not in visited:
                dfs(node,visited)
                provinces += 1
            
        return provinces