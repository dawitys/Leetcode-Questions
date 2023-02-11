class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s,e in redEdges:
            graph[s].append((e,0))
            
        for s,e in blueEdges:
            graph[s].append((e,1))
        
        ans = [[inf,inf] for _ in range(n)]
        queue = deque([(0,0,0),(0,1,0)])
        
        visited = set([(0,0),(0,1)])

        while queue:
            curr,color,step = queue.popleft()
            ans[curr][color] = step

            for ne, c in graph[curr]:
                if c != color and (ne,c) not in visited:
                    queue.append((ne,c,step+1))
                    visited.add((ne,c))
                    
        return [min(ans[i]) if min(ans[i]) != inf else -1 for i in range(n)]
                