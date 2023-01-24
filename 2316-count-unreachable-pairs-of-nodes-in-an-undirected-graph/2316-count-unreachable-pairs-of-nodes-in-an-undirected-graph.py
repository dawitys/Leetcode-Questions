class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
            
        seen = set()
        def dfs(node):
            count = 0
            seen.add(node)
            for ne in graph[node]:
                if ne not in seen:
                    count += dfs(ne)
                    
            return count + 1
                
        ans = 0
        nodes = 0
        for i in range(n):
            if i not in seen:
                c = dfs(i)
                ans += c*nodes
                nodes += c

                    
        return ans