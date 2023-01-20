class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(node, prev):
            
            steps = 0
            for ne in graph[node]:
                if ne != prev:
                    steps += dfs(ne, node)
            
            return steps + 2 if hasApple[node] or steps else 0
        
        return max(dfs(0,-1) - 2,0)