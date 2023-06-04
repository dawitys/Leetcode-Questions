class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        uf = [i for i in range(n)]
        siz = [1 for i in range(n)]
        
        def find(i):
            if uf[i] == i:
                return uf[i]
            uf[i] = find(uf[i])
            return uf[i]
        
        def union(i,j):
            pi =find(i)
            pj = find(j)
            if siz[pi] > siz[pj]:
                pi,pj = pj,pi
            uf[pj] = uf[pi]
            siz[pi] += siz[pj]
            
        def connected(i,j):
            return find(i) == find(j)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i,j)
                    
            
        return len(set([find(i) for i in range(n)]))