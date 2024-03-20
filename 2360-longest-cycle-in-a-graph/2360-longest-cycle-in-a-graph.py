class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        distance = [-1] * len(edges)
        ans = -1
        
        def dfs(node,d):
            if node == -1:
                return
            nonlocal ans
            if distance[node] == -1:
                distance[node] = d  
                visited.add(node)
                dfs(edges[node],d+1)
            elif node in visited:
                ans = max(ans, d - distance[node])

              
        for i in range(len(edges)):
            if distance[i] == -1:
                visited = set()
                dfs(edges[i],1)
                
        return ans