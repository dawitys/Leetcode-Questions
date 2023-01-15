class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]* n for _ in range(n)]
        
        for rs,cs,re,ce in queries:
            for i in range(rs,re+1):
                matrix[i][cs] += 1
                if ce < n-1:
                    matrix[i][ce+1] -= 1
        
        for i in range(n):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]

        return matrix