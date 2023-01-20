class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for start, destination in edges:
            graph[start].append(destination)
            graph[destination].append(start)
        
        same_label_subtrees = [1] * n
        
        def dfs(node,parent):
            res = defaultdict(int)
            for ne in graph[node]:
                if ne != parent:
                    subtrees = dfs(ne,node)
                    for subtree in subtrees:
                        if subtree == labels[node]:
                            same_label_subtrees[node] += subtrees[subtree]
                        res[subtree] += subtrees[subtree]
                 
            res[labels[node]] += 1  

            return res
        
        dfs(0,None)
        return same_label_subtrees
            
        