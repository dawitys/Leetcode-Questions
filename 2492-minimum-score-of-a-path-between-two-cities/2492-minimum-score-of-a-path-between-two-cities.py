class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for s,e,w in roads:
            graph[s].append((e,w))
            graph[e].append((s,w))
        
        vis = {}

        def dfs(node,ms,vis):
            vis[node] = ms
            min_score = ms
            
            for ne,we in graph[node]:
                if ne not in vis or vis[ne] > we:
                    t = dfs(ne,min(min_score,we),vis)
                    min_score = min(min_score,t)
                else:
                    min_score = min(min_score,vis[ne])
 
            return min_score
        
        res = math.inf
        for ne,we in graph[1]:
            res = min(res,dfs(ne,we,vis))
            
        return res