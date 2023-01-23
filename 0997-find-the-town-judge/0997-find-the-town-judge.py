class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [0] * n
        non_judges = set()
        
        for s,e in trust:
            graph[e-1] += 1
            non_judges.add(s-1)
            
        for i in range(n):
            if graph[i] == n-1 and i not in non_judges:
                return i+1
            
        return -1
            
