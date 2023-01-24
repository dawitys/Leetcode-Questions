class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [0] * n
        non_judges = set()
        
        for s,e in trust:
            graph[e-1] += 1
            graph[s-1] -= 1
            
        for i in range(n):
            if graph[i] == n-1:
                return i+1
            
        return -1
            
