from heapq import heappush,heappop
    
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        graph = defaultdict(list)
        
        for start, destination,weight in edges:
            graph[start].append((destination,weight))
            graph[destination].append((start,weight))
        
        priority_queue = [(0,n)]
        visited = {n:0}
        
        while priority_queue:
            min_dist, current_node = heappop(priority_queue)

            for neighbour,cost in graph[current_node]:
                if neighbour not in visited or visited[neighbour] > min_dist+cost:
                    heappush(priority_queue,(min_dist+cost,neighbour))
                    visited[neighbour] = min_dist + cost
                    
        seen = set()
        
        @lru_cache(None)
        def dfs(node):
            count = int(node==n)
            for ne,_ in graph[node]:
                if visited[ne] < visited[node]:
                    count += dfs(ne) % MOD   
            return count % MOD
        
        return dfs(1)
                