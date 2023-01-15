class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        @cache
        def dfs(node,parent):
            total = 0
            for ne in graph[node]:
                if ne != parent:
                    total = max(total,dfs(ne,node))
                    
            return total + price[node]
        
        ans = 0
        
        for i in range(n):
            min_price = price[i]
            max_price = dfs(i,None)
            
            ans = max(ans, max_price - min_price)
            
        return ans