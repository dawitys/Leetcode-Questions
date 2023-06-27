class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        conn = set()
        
        for start,destination in connections:
            graph[start].append(destination)
            graph[destination].append(start)
            
            conn.add((start,destination))
        
        def dfs(node,visited):
            cost = 0
            for ne in graph[node]:
                if ne not in visited:
                    visited.add(ne)
                    cost += int((node,ne) in conn) + dfs(ne,visited)
                    
                    
            return cost  

        vis = set({0})
        return dfs(0,vis)