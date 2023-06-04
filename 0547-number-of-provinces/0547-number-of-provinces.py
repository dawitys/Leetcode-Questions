class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        uf = [i for i in range(n)]
        
        def find(i):
            while uf[i] != i:
                i = uf[i]
            return i
        def union(i,j):
            pi =find(i)
            pj = find(j)
            uf[pj] = uf[pi]
            
        def connected(i,j):
            return find(i) == find(j)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i,j)
                    
            
        return len(set([find(i) for i in range(n)]))