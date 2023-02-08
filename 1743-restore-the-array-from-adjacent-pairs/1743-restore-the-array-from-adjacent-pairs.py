class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for n1,n2 in adjacentPairs:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        ans = []
        def dfs(node,parent):
            ans.append(node)
            for ne in graph[node]:
                if ne != parent:
                    dfs(ne,node)
                
        for n in graph:
            if len(graph[n]) == 1:
                dfs(n,None)
                break
                
        return ans